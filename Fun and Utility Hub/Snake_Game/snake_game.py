from turtle import Screen
from .snake import Snake
from .scoreboard import Scoreboard

class SnakeGame:

    def __init__(self):
        self.screen = Screen()
        self.screen.title("Snake Game")
        self.screen.setup(height=600, width=600)
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        self.python = Snake()
        self.screen.listen()
        self.screen.onkey(self.python.up, "Up")
        self.screen.onkey(self.python.down, "Down")
        self.screen.onkey(self.python.left, "Left")
        self.screen.onkey(self.python.right, "Right")
        self.scoreboard = Scoreboard()

    def run_game(self):
        self.python.move()
        self.screen.exitonclick()



