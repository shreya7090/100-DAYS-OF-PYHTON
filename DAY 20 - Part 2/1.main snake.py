from turtle import Screen
from snake_class import Snake
from food_class import Food
from scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Create snake
snake = Snake()

# Create food object
food = Food()

# Create scoreboard
scoreboard = Scoreboard()

# Listen for key presses
screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_scoreboard()

    # Check for wall collision
    if (
        snake.head.xcor() > 280 or snake.head.xcor() < -280
        or snake.head.ycor() > 280 or snake.head.ycor() < -280
    ):
        game_on = False
        scoreboard.game_over()

    # Detect collision with tail (only when length > 2)
    if len(snake.snake_body) > 2:
        for segment in snake.snake_body[1:]:
            if snake.head.distance(segment) < 10:
                game_on = False
                scoreboard.game_over()

screen.exitonclick()
