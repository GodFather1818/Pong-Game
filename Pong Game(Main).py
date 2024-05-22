import turtle
# Step 1: Creating the main screen.

from turtle import *
from paddle import Paddle
from ball import Ball
import time
from scoreboard_pong_game import Scoreboard

turtle.tracer(0)
screen = Screen()
screen.bgcolor('black')
screen.setup(height=600, width=800)
screen.title('Pong Game')

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()

screen.onkey(key='Up', fun=r_paddle.up)
screen.onkey(key='Down', fun=r_paddle.down)
screen.onkey(key='w', fun=l_paddle.up)
screen.onkey(key='s', fun=l_paddle.down)


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detecting collisions with the upper wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

#     Detecting the collisions with the right paddles.
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        # print("Contact Made")
        ball.bounce_x()
#     Detect when right paddle misses.
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
