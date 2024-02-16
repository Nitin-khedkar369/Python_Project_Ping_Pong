from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreborad import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

right = Paddle(350, 0)

left = Paddle(-350, 0)

ball = Ball()

score = Scoreboard()

screen.listen()
screen.onkey(right.up, "Up")
screen.onkey(right.down, "Down")
screen.onkey(left.up, "w")
screen.onkey(left.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with right paddle
    if ball.distance(right) < 50 and ball.xcor() > 320 or ball.distance(left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()



screen.exitonclick()