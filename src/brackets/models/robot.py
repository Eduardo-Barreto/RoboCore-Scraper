class Robot:
    def __init__(self, name, team):
        self.name = name
        self.team = team

    def to_dict(self):
        return {
            "name": self.name,
            "team": self.team,
        }
