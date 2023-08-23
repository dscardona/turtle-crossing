from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color("red")
        self.penup()
        self.goto(300, 0)
        self.move_left()

    def move_left(self):
        new_x = self.xcor() - MOVE_INCREMENT
        self.goto(new_x, self.ycor())
