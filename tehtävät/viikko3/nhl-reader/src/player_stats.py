class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        x = [player for player in players if player.nationality == nationality]
        y = sorted(x,key=lambda player:player.points,reverse=True)

        return y