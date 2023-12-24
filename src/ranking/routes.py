from flask import Blueprint, jsonify
from ranking.controller import RankingController
import logging

ranking_bp = Blueprint("ranking", __name__)
controller = RankingController()


@ranking_bp.route("/<category>")
def get_ranking(category: str) -> str:
    try:
        result = controller.get_ranking(category)

        if "error" in result:
            return jsonify(result), result["status_code"]
        else:
            return jsonify(result)

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return jsonify(
            {"error": "An unexpected error occurred", "status_code": 500}
        ), 500
