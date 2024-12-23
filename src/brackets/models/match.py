from brackets.models.robot import Robot


class Match:
    def __init__(self, winner: Robot, loser: Robot):
        self.winner = winner
        self.loser = loser

    def to_dict(self):
        return {
            "winner": self.winner.to_dict(),
            "loser": self.loser.to_dict(),
        }
