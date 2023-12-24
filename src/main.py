import json
from history.scraper import fetch_robot_data
from history.parser import extract_robot_data, extract_event_data, extract_matches
from history.models import Robot


def pipeline(robot_id):
    soup = fetch_robot_data(robot_id)
    robot = extract_robot_data(soup, robot_id)

    events = soup.find_all("div", class_="panel panel-default")
    event_id_counter = 1
    robot.events = [
        extract_event_data(event, robot.name, f"{robot_id}_{event_id_counter}")
        for event in events
    ]
    event_id_counter += 1

    return robot


def main():
    robot_id = "963"
    robot = pipeline(robot_id)

    with open("result.json", "w") as f:
        json.dump(robot.to_dict(), f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()
