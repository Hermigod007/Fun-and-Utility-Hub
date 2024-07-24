from turtle import Turtle, Screen
import time
from .food import Food
from .scoreboard import Scoreboard

MOVE_DISTANCE = 20
UP = 90
DOWN = -90
RIGHT = 0
LEFT = 180

class Snake:
    snake_body = []
    INITIAL_POSITION = [(0, 0), (-20, 0), (-40, 0)]

    def __init__(self):
        self.create_snake()

    def create_snake(self):
        for position in self.INITIAL_POSITION:
            self.create_segment(position)

    def move(self):
        food = Food()
        screen = Screen()
        s = Scoreboard()
        while True:
            screen.update()
            time.sleep(0.1)

            for seg_num in range(len(self.snake_body) - 1, 0, -1):
                new_x = self.snake_body[seg_num - 1].xcor()
                new_y = self.snake_body[seg_num - 1].ycor()
                self.snake_body[seg_num].goto(new_x, new_y)
            self.snake_body[0].forward(MOVE_DISTANCE)

            if self.snake_body[0].distance(food) < 15:
                food.refresh()
                self.extend()
                s.increase_score()
                self.extend()

            if self.snake_body[0].xcor() >= 300 or self.snake_body[0].xcor() <= -300:
                s.reset_score()
                self.reset()
                break
            elif self.snake_body[0].ycor() >= 300 or self.snake_body[0].ycor() <= -300:
                s.reset_score()
                self.reset()
                break

            self.collison(s)

    def reset(self):
        self.create_snake()


    def collison(self,sc):

        for parts in self.snake_body:

            if parts == self.snake_body[0]:
                pass
            elif parts.distance(self.snake_body[0]) < 10:
                sc.reset_score()
                self.reset()
                break

    def create_segment(self, position):
        snake = Turtle(shape="square")
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.snake_body.append(snake)

    def extend(self):
        self.create_segment(self.snake_body[-1].position())

    def up(self):
        if self.snake_body[0].heading() != DOWN:
            self.snake_body[0].setheading(UP)

    def down(self):
        if self.snake_body[0].heading() != UP:
            self.snake_body[0].setheading(DOWN)

    def right(self):
        if self.snake_body[0].heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)

    def left(self):
        if self.snake_body[0].heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)
