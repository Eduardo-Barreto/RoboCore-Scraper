from flask import Blueprint, jsonify
from history.controller import HistoryController
import logging

history_bp = Blueprint("history", __name__)
controller = HistoryController()


@history_bp.route("/<robot_id>")
def get_history(robot_id: str) -> str:
    try:
        result = controller.get_robot_history(robot_id)

        if "error" in result:
            return jsonify(result), result["status_code"]
        else:
            return jsonify(result)

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return jsonify(
            {"error": "An unexpected error occurred", "status_code": 500}
        ), 500
