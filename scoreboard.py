from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self. penup()
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-230, 270)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_score(self):
        self.level += 1
        self.update_scoreboard()