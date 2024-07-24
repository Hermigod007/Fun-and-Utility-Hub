from turtle import Turtle
class Paddles(Turtle):

    def __init__(self, x_cord, y_cord):
        super().__init__()

        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.goto(x_cord, y_cord)

    def up(self):
        new_y = self.ycor() + 38
        self.goto(x=self.xcor(), y=new_y)

    def down(self):
        new_y = self.ycor() - 38
        self.goto(x=self.xcor(), y=new_y)



