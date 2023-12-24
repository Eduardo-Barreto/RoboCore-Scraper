from typing import List
from history.models.match import Match


class Event:
    def __init__(
        self,
        name: str,
        location: str,
        start_date: str,
        end_date: str,
        matches: List[Match],
    ):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.matches = matches

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "location": self.location,
            "startDate": self.start_date,
            "endDate": self.end_date,
            "matches": [match.to_dict() for match in self.matches],
        }
