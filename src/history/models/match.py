class Match:
    def __init__(self, opponent: str, opponent_id: str, winner: str):
        self.opponent = opponent
        self.opponent_id = opponent_id
        self.winner = winner

    def to_dict(self) -> dict:
        return {
            "opponent": self.opponent,
            "opponentId": self.opponent_id,
            "winner": self.winner,
        }
