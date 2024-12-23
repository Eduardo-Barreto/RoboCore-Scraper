from bs4 import BeautifulSoup
from typing import List
from history.models.event import Event
from history.models.match import Match
from history.models.robot import Robot
import logging


def parse_robot_data(soup: BeautifulSoup, robot_id: str) -> Robot:
    try:
        robot_name = soup.find("h2").text.strip().replace("score history", "")
        robot_team = soup.find("p").text.strip()
        robot_category = soup.find("p", style="color: gray;").text.strip()

        robot = Robot(
            robot_id.strip(),
            robot_name.strip(),
            robot_team.strip(),
            robot_category.strip(),
            [],
        )
        events = soup.find_all("div", class_="panel panel-default")

        for event in events:
            parsed_event = parse_event_data(event, robot_name)
            robot.events.append(parsed_event)

        return robot
    except AttributeError as e:
        logging.error(f"An error occurred while parsing robot data: {e}")
        return Robot(robot_id, "N/A", "N/A", "N/A", [])


def parse_event_data(event: BeautifulSoup, robot_name: str) -> Event:
    event_name = event.find("h3").text.split("\n")[0].strip()
    ul_items = event.find("ul").find_all("li")
    event_location = ul_items[0].text.strip()
    event_start_date, event_end_date = ul_items[1].text.split(" - ")
    event_start_date = event_start_date.strip("\t")
    event_end_date = event_end_date.strip("\t")

    matches = parse_matches(event, robot_name)
    return Event(
        event_name.strip(),
        event_location.strip(),
        event_start_date.strip(),
        event_end_date.strip(),
        matches
    )


def parse_matches(event: BeautifulSoup, robot_name: str) -> List[Match]:
    matches = event.find("tbody").find_all("tr")
    parsed_matches = []

    for match in matches:
        result = match.find_all("td")[1]
        opponent = " ".join(result.text.split()[2:])
        opponent_id = match.find("a")["href"].replace("/history/", "")
        winner = robot_name if "won" in result.text.lower() else opponent
        parsed_matches.append(
            Match(opponent.strip(), opponent_id.strip(), winner.strip())
        )

    return parsed_matches
