from turtle import Turtle, Screen
import random

class TurtleRace:
    def __init__(self):
        self.turtle_colors = ["red", "green", "yellow", "blue", "purple", "black"]
        self.positions = [100, 50, 0, -50, -100]
        self.screen = Screen()
        self.screen.setup(height=400, width=500)
        self.user_choice = self.screen.textinput(title="Do you wanna bet", prompt="Which turtle do you choose?")
        self.turtles_list = []

    def setup_race(self):
        for index, color in enumerate(self.turtle_colors[:5]):
            turtle = Turtle(shape="turtle")
            turtle.penup()
            turtle.goto(x=-230, y=self.positions[index])
            turtle.color(color)
            self.turtles_list.append(turtle)

    def start_race(self):
        while True:
            choice = random.choice(self.turtles_list)
            choice.forward(5)
            x_position = choice.xcor()
            if x_position >= 230:
                print(f"The winner of the race is {choice.color()[0]}")
                if self.user_choice != choice.color()[0]:
                    print("Sorry, You lost...")
                else:
                    print("Congratulations, your turtle won!")
                break

    def run(self):
        self.setup_race()
        self.start_race()
        self.screen.exitonclick()

if __name__ == "__main__":
    race = TurtleRace()
    race.run()
