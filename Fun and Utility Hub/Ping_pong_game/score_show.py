from turtle import Turtle

class Scorecard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,250)

    def show_score_left(self):
        self.write(f"{self.score}", align="left", font=("Arial", 24, "normal"))
        self.clear()

    def show_score_right(self):
        self.write(f"{self.score} : ", align="right", font=("Arial", 24, "normal"))
        self.clear()


    def increase_score_left(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", align="left", font=("Arial", 24, "normal"))

    def increase_score_right(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score} : ", align="right", font=("Arial", 24, "normal"))
