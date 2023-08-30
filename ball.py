from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.shape("circle")
        self.goto(x=0, y=0)

        self.x_move = 10
        self.y_move = 10

        self.accelerator = 0.1
        pass

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(new_x, new_y)
        pass

    def top_bounce(self):
        self.y_move *= -1
        pass

    def paddle_bounce(self):
        self.x_move *= -1
        self.accelerator *= 0.8
        pass

    def reset_pos(self):
        self.goto(x=0, y=0)
        self.accelerator = 0.1
        self.paddle_bounce()
