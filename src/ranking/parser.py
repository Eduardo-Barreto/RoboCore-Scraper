from bs4 import BeautifulSoup
from typing import List
from ranking.models.robot import Robot
import logging


def parse_ranking_data(soup: BeautifulSoup, category: str) -> dict:
    try:
        robots = []

        rank_table = soup.find("table", class_="table table-striped table-hover rank")
        rows = rank_table.find("tbody").find_all("tr")

        for row in rows:
            columns = row.find_all("td")
            position = columns[0].text.strip()
            score = columns[1].text.strip()
            robot_name = columns[2].find("a").text.strip()
            robot_id = columns[2].find("a")["href"].replace("/history/", "")
            team = columns[2].text.split("\n ")[1].strip()
            team_country = columns[2].find("span", class_="flag-icon")["title"]
            total_fights = columns[3].text.strip()
            total_wins, total_losses = columns[4].text.strip().split("/")
            latest_fight = columns[5].text.strip()

            robot = Robot(
                position,
                score,
                robot_name,
                robot_id,
                team,
                team_country,
                total_fights,
                total_wins,
                total_losses,
                latest_fight,
            )

            robots.append(robot.to_dict())

        return {"category": category, "ranking": robots}

    except Exception as e:
        logging.error(f"An error occurred while parsing ranking data: {e}")
        raise RuntimeError(f"An error occurred while parsing ranking data: {e}")
