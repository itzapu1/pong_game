from turtle import Turtle

PADDLE_WIDTH = 5
PADDLE_LENGTH = 1


class Paddle(Turtle):
    """ create a paddle"""

    def __init__(self, paddle_position):
        super().__init__()
        self.penup()

        self.goto(paddle_position)
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LENGTH, outline=None)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

