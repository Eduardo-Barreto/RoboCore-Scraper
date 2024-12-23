from flask import Blueprint, jsonify
from brackets.controller import BracketController
import logging

brackets_bp = Blueprint("brackets", __name__)
controller = BracketController()


@brackets_bp.route("/<event_id>/<category_id>")
def get_brackets(event_id: str, category_id: str) -> tuple:
    try:
        result = controller.get_event_brackets(event_id, category_id)

        if "error" in result:
            return jsonify(result), result["status_code"]
        else:
            return jsonify(result)

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return (
            jsonify({"error": "An unexpected error occurred", "status_code": 500}),
            500,
        )
