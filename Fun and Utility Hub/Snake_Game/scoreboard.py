from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:
            contents = file.read()
        self.high_score = int(contents)
        self.goto(x=0, y=260)
        self.color("white")
        self.write(f"Score : {self.score}", align="right", font=("Arial", 24, "normal"))
        self.write(f"  High Score : {self.high_score}", align="left", font=("Arial", 24, "normal"))
        self.hideturtle()
        self.penup()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score}", align="right", font=("Arial", 24, "normal"))
        self.write(f"  High Score : {self.high_score}", align="left", font=("Arial", 24, "normal"))
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def reset_score(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_scoreboard()
            self.score = 0



