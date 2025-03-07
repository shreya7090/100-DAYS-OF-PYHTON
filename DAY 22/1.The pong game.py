from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Create the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

# Create paddles, ball, and scoreboard
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()  

# Control paddle movement
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeyrelease(r_paddle.stop_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeyrelease(r_paddle.stop_down, "Down")

screen.onkeypress(l_paddle.go_up, "w")
screen.onkeyrelease(l_paddle.stop_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkeyrelease(l_paddle.stop_down, "s")


game_on = True
while game_on:
    time.sleep(ball.move_speed)  
    screen.update()
    ball.move()

    # Detect collision with walls (top & bottom)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect when the right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point() 

    # Detect when the left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()  

screen.exitonclick()
