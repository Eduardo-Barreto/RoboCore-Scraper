class Match:
    def __init__(self, opponent, opponent_id, winner):
        self.opponent = opponent
        self.opponent_id = opponent_id
        self.winner = winner

    def to_dict(self):
        return {
            "opponent": self.opponent,
            "opponentId": self.opponent_id,
            "winner": self.winner,
        }


class Event:
    def __init__(self, event_id, name, location, start_date, end_date, matches):
        self.event_id = event_id
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.matches = matches

    def to_dict(self):
        return {
            "eventId": self.event_id,
            "name": self.name,
            "location": self.location,
            "startDate": self.start_date,
            "endDate": self.end_date,
            "matches": [match.to_dict() for match in self.matches],
        }


class Robot:
    def __init__(self, robot_id, name, team, category, events):
        self.robot_id = robot_id
        self.name = name
        self.team = team
        self.category = category
        self.events = events

    def to_dict(self):
        return {
            "robotId": self.robot_id,
            "name": self.name,
            "team": self.team,
            "category": self.category,
            "events": [event.to_dict() for event in self.events],
        }
