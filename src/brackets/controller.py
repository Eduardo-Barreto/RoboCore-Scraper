from brackets.parser import parse_brackets
from brackets.scraper import fetch_event_data
import logging


class BracketController:
    def get_event_brackets(self, event_id: str, category_id: str) -> dict:
        try:
            soup = fetch_event_data(event_id, category_id)
            return parse_brackets(soup, event_id, category_id)
        except FileNotFoundError:
            logging.warning(f"No data found for event {event_id} in category {category_id}")
            return {"error": "Data not found", "status_code": 404}
        except Exception as e:
            logging.error(f"An error occurred while processing brackets: {e}")
            return {"error": "Failed to process data", "status_code": 500}
