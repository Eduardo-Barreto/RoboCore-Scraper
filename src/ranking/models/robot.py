class Robot:
    def __init__(
        self,
        position: str,
        score: str,
        robot_name: str,
        robot_id: str,
        team: str,
        team_country: str,
        total_fights: str,
        total_wins: str,
        total_losses: str,
        latest_fight: str,
    ):
        self.position = position
        self.score = score
        self.robot_name = robot_name
        self.robot_id = robot_id
        self.team = team
        self.team_country = team_country
        self.total_fights = total_fights
        self.total_wins = total_wins
        self.total_losses = total_losses
        self.latest_fight = latest_fight

    def to_dict(self) -> dict:
        return {
            "position": self.position,
            "score": self.score,
            "robotName": self.robot_name,
            "robotID": self.robot_id,
            "team": self.team,
            "teamCountry": self.team_country,
            "totalFights": self.total_fights,
            "totalWins": self.total_wins,
            "totalLosses": self.total_losses,
            "latestFight": self.latest_fight,
        }
