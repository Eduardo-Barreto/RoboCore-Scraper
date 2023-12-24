import requests
from bs4 import BeautifulSoup, Comment


def fetch_robot_data(robot_id: str) -> BeautifulSoup:
    base_url: str = "https://rank.robocore.net/history"
    url: str = f"{base_url}/{robot_id}"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    for comment in comments:
        comment.extract()

    for unwanted_tag in ["style", "script"]:
        for tag in soup.find_all(unwanted_tag):
            tag.extract()

    return soup.body
