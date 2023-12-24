from typing import List
from history.models.event import Event


class Robot:
    def __init__(
        self, robot_id: str, name: str, team: str, category: str, events: List[Event]
    ):
        self.robot_id = robot_id
        self.name = name
        self.team = team
        self.category = category
        self.events = events

    def to_dict(self) -> dict:
        return {
            "robotId": self.robot_id,
            "name": self.name,
            "team": self.team,
            "category": self.category,
            "events": [event.to_dict() for event in self.events],
        }
