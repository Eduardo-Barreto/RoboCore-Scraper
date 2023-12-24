from flask import Blueprint, jsonify
from history.controller import HistoryController

history_bp = Blueprint("history", __name__)
controller = HistoryController()


@history_bp.route("/<robot_id>")
def get_history(robot_id: str) -> str:
    result = controller.get_robot_history(robot_id)
    print(result)
    return jsonify(result)
