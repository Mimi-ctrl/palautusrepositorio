class Player:
    def __init__(self, name, team, nationality, goals, assists):
        self.name = name
        self.team = team
        self.nationality = nationality
        self.goals = goals
        self.assists = assists

    @property
    def points(self):
        return self.goals + self.assists
    
    def __str__(self):
        return f"{self.name:22} {self.team:1} {self.goals:3} + {self.assists:2} = {self.points}"
