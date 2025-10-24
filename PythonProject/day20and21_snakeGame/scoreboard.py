from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score =0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)

    def refresh_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, ALIGNMENT, FONT)