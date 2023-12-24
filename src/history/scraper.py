import requests
from bs4 import BeautifulSoup, Comment
import logging


def fetch_robot_data(robot_id: str) -> BeautifulSoup:
    base_url: str = "https://rank.robocore.net/history"
    url: str = f"{base_url}/{robot_id}"

    try:
        response = requests.get(url)

        if response.status_code == 404 or "Robot info not found" in response.text:
            logging.warning(f"Robot info not found for robot {robot_id}")
            raise FileNotFoundError(f"Robot info not found for robot {robot_id}")

        response.raise_for_status()

    except requests.exceptions.HTTPError as e:
        logging.error(f"Failed to fetch data for robot {robot_id}: {e}")
        raise RuntimeError(f"Failed to fetch data for robot {robot_id}: {e}")

    soup = BeautifulSoup(response.text, "html.parser")

    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    for comment in comments:
        comment.extract()

    for unwanted_tag in ["style", "script"]:
        for tag in soup.find_all(unwanted_tag):
            tag.extract()

    return soup.body
