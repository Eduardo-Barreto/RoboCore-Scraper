from bs4 import BeautifulSoup
import logging
import requests
from typing import List, Dict


def organize_matches(matches: List[Dict]) -> Dict[str, List[Dict]]:
    """
    Organize matches into losers and winners brackets.

    Args:
        matches (List[Dict]): List of match data dictionaries.

    Returns:
        Dict[str, List[Dict]]: Organized matches with 'losers_bracket' and 'winners_bracket'.
    """
    robot_losses = {}
    losers_bracket = []
    winners_bracket = []

    for match in matches:
        loser = match["loser"]["robot"]
        robot_losses[loser] = robot_losses.get(loser, 0) + 1

    is_losers = True
    for match in matches:
        loser = match["loser"]["robot"]
        if robot_losses[loser] == 3:
            is_losers = False

        if is_losers:
            losers_bracket.append(match)
        else:
            winners_bracket.append(match)

        robot_losses[loser] = robot_losses.get(loser, 0) + 1

    losers_bracket.reverse()

    return {
        "losers_bracket": losers_bracket,
        "winners_bracket": winners_bracket,
    }


def parse_brackets(soup: BeautifulSoup, event_id: str, category_id: str) -> dict:
    """
    Parse the tournament brackets from the HTML content.

    Args:
        soup (BeautifulSoup): Parsed HTML content.
        event_id (str): Event identifier.
        category_id (str): Category identifier.

    Returns:
        dict: Organized matches into losers and winners brackets.
    """
    try:
        main_table = soup.find("table", {"id": "tblBracket"})
        match_links = main_table.find_all("a", {"data-src": True})
        # remove o primeiro link
        match_links.pop(0)

        matches = []

        for link in match_links:
            if ">>" not in link.get_text(strip=True) and "<<" not in link.get_text(
                strip=True
            ):
                continue

            winner_name = (
                link.get_text(strip=True).replace(">>", "").replace("<<", "").strip()
            )

            data_src = link["data-src"]
            match_data = parse_match_details(
                data_src, winner_name, event_id, category_id
            )
            matches.append(match_data)

        organized_brackets = organize_matches(matches)

        return organized_brackets
    except Exception as e:
        logging.error(f"An error occurred while parsing brackets: {e}")
        raise RuntimeError("Failed to parse brackets")


def parse_match_details(
    data_src: str, winner_name: str, event_id: str, category_id: str
) -> dict:
    """
    Parse match details from the provided data source.

    Args:
        data_src (str): Data source URL for the match.
        winner_name (str): Name of the winning robot.
        event_id (str): Event identifier.
        category_id (str): Category identifier.

    Returns:
        dict: Match details with winner and loser information.
    """
    base_url: str = "https://events.robocore.net"
    url: str = f"{base_url}/{event_id}/brackets/{category_id}"
    match_url = f"{url}{data_src}"
    match_response = requests.get(match_url)
    match_soup = BeautifulSoup(match_response.text, "html.parser")

    team_names = [
        team.get_text(strip=True)
        for team in match_soup.find_all("div", {"class": "team_name"})
    ]
    team_robots = [
        robot.get_text(strip=True)
        for robot in match_soup.find_all("div", {"class": "team_robot"})
    ]

    if len(team_names) < 2 or len(team_robots) < 2:
        raise ValueError("Informações de equipes incompletas na partida.")
    winner_index = 0 if winner_name in team_robots[0] else 1

    return {
        "winner": {
            "name": team_names[winner_index],
            "robot": team_robots[winner_index],
        },
        "loser": {
            "name": team_names[1 - winner_index],
            "robot": team_robots[1 - winner_index],
        },
    }
