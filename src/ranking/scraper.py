import requests
from bs4 import BeautifulSoup, Comment
import logging


def fetch_ranking_data(category: str) -> BeautifulSoup:
    base_url: str = "https://rank.robocore.net"
    url: str = f"{base_url}/{category}"

    try:
        response = requests.get(url)

        if response.status_code == 404 or "Found no results" in response.text:
            logging.warning(f"Ranking info not found for category {category}")
            raise FileNotFoundError(f"Ranking info not found for category {category}")

        response.raise_for_status()

    except requests.exceptions.HTTPError as e:
        logging.error(f"Failed to fetch ranking data for category {category}: {e}")
        raise RuntimeError(f"Failed to fetch ranking data for category {category}: {e}")

    soup = BeautifulSoup(response.text, "html.parser")

    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    for comment in comments:
        comment.extract()

    for unwanted_tag in ["style", "script"]:
        for tag in soup.find_all(unwanted_tag):
            tag.extract()

    return soup.body
