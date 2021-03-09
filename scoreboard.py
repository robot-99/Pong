from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.player_1 = 0
        self.player_2 = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 240)
        self.write(self.player_2, align="center", font=("Arial", 40, "normal"))
        self.goto(100, 240)
        self.write(self.player_1, align="right", font=("Arial", 40, "normal"))

    def player2_point(self):
        self.player_2 += 1
        self.update_scoreboard()

    def player1_point(self):
        self.player_1 += 1
        self.update_scoreboard()