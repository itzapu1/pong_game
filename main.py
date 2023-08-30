from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)

screen.bgcolor("black")
screen.title("Welcome to the game of pong")
screen.setup(width=800, height=600)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()
scoreboard.print_score()

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.accelerator)
    screen.update()
    ball.move()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.top_bounce()

    # detect a collision ith paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < - 320:
        ball.paddle_bounce()

    # detect when the right paddle misses the ball
    if ball.xcor() > 390:
        scoreboard.add_l_score()
        ball.reset_pos()

    # detect when the left paddle misses the ball
    if ball.xcor() < -390:
        scoreboard.add_r_score()
        ball.reset_pos()

screen.exitonclick()
