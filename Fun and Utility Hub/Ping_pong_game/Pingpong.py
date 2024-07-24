from turtle import Screen
from .paddles import Paddles
from .ball import Ball
from .score_show import Scorecard
import time

class PingPongGame:

    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Ping-Pong Game")
        self.screen.tracer(0)

        self.r_paddle = Paddles(350, 0)
        self.l_paddle = Paddles(-350, 0)
        self.ball = Ball()
        self.right_score = Scorecard()
        self.left_score = Scorecard()

        self.right_score.show_score_right()
        self.left_score.show_score_left()

        self.setup_controls()
        self.game_is_on = True

    def setup_controls(self):
        self.screen.listen()
        self.screen.onkey(self.r_paddle.up, "Up")
        self.screen.onkey(self.r_paddle.down, "Down")
        self.screen.onkey(self.l_paddle.up, "w")
        self.screen.onkey(self.l_paddle.down, "s")

    def play(self):
        while self.game_is_on:
            time.sleep(self.ball.move_speed)
            self.screen.update()
            self.ball.move()

            # Ball collision with top or bottom walls
            if self.ball.ycor() >= 280 or self.ball.ycor() <= -280:
                self.ball.bounce_y()

            # Ball out of bounds
            if self.ball.xcor() >= 400 or self.ball.xcor() <= -400:
                if self.ball.xcor() >= 400:
                    self.left_score.increase_score_right()
                else:
                    self.right_score.increase_score_left()

                self.ball.restart()

            # Ball collision with paddles
            if self.r_paddle.distance(self.ball) < 50 and self.ball.xcor() > 320:
                self.ball.bounce_x()
            elif self.l_paddle.distance(self.ball) < 50 and self.ball.xcor() < -320:
                self.ball.bounce_x()

        self.screen.exitonclick()



