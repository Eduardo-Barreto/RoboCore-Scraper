import requests
from bs4 import BeautifulSoup, Comment
import logging


def fetch_event_data(event_id: str, category_id: str) -> BeautifulSoup:
    base_url: str = "https://events.robocore.net"
    url: str = f"{base_url}/{event_id}/brackets/{category_id}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        if "No data found" in response.text:
            logging.warning(f"No data found for event {event_id} in category {category_id}")
            raise FileNotFoundError(f"No data found for event {event_id} in category {category_id}")

    except requests.exceptions.HTTPError as e:
        logging.error(f"Failed to fetch data for event {event_id} in category {category_id}: {e}")
        raise RuntimeError(f"Failed to fetch data: {e}")

    soup = BeautifulSoup(response.text, "html.parser")

    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    for comment in comments:
        comment.extract()

    for unwanted_tag in ["style", "script"]:
        for tag in soup.find_all(unwanted_tag):
            tag.extract()

    return soup.body
