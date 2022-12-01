class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0
        self.score2 = 0
        self.scoring = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty", 4: "Deuce"}

    def won_point(self, player_name):
        if player_name == self.player1:
            self.score1 = self.score1 + 1
        else:
            self.score2 = self.score2 + 1

    def get_score(self):
        if self.score1 == self.score2:
            if self.score1 < 4:
                return self.scoring[self.score1] + "-All"
            return self.scoring[4]
        if self.score1 >= 4 or self.score2 >= 4:
            muuta = self.score1 - self.score2
            if muuta == 1:
                return "Advantage: Player 1"
            if muuta == -1:
                return "Advantage: Player 2"
            if muuta >= 2:
                return "Winner: Player 1"
            return "Winner: Player 2"
        return self.scoring[self.score1] + "-" + self.scoring[self.score2]
 