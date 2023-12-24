from history.parser import parse_robot_data
from history.scraper import fetch_robot_data


class HistoryController:
    def get_robot_history(self, robot_id: str) -> dict:
        soup = fetch_robot_data(robot_id)
        return parse_robot_data(soup, robot_id).to_dict()
