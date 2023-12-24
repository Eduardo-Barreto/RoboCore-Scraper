from history.parser import parse_robot_data
from history.scraper import fetch_robot_data
import logging


class HistoryController:
    def get_robot_history(self, robot_id: str) -> dict:
        try:
            soup = fetch_robot_data(robot_id)
            return parse_robot_data(soup, robot_id).to_dict()
        except FileNotFoundError:
            logging.warning(f"Robot info not found for robot {robot_id}")
            return {"error": "Robot info not found", "status_code": 404}
        except Exception as e:
            logging.error(f"An error occurred while processing robot history: {e}")
            return {"error": "Failed to process robot history", "status_code": 500}
