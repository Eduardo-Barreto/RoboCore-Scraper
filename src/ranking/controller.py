from ranking.parser import parse_ranking_data
from ranking.scraper import fetch_ranking_data
import logging


class RankingController:
    def get_ranking(self, category: str) -> dict:
        try:
            soup = fetch_ranking_data(category)
            return parse_ranking_data(soup, category)
        except FileNotFoundError:
            logging.warning(f"Ranking info not found for category {category}")
            return {
                "error": f"Ranking info not found for category {category}",
                "status_code": 404,
            }
        except Exception as e:
            logging.error(f"An error occurred while processing ranking data: {e}")
            return {
                "error": f"Failed to process ranking data for category {category}",
                "status_code": 500,
            }
