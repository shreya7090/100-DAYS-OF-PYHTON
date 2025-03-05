from turtle import Screen, Turtle
import time  # To control speed
import random  # To generate random positions

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turns off automatic updates

# Create the snake body
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
snake_body = []

for position in starting_positions:
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    snake_body.append(segment)

# Create food object
food = Turtle("circle")
food.color("blue")
food.shapesize(0.35, 0.35)
food.penup()

# Function to place food in a random position
def move_food():
    new_x = random.randint(-280, 280)
    new_y = random.randint(-280, 280)
    food.goto(new_x, new_y)

move_food()  # Place food initially

# Movement functions
def move_up():
    if snake_body[0].heading() != 270:
        snake_body[0].setheading(90)

def move_down():
    if snake_body[0].heading() != 90:
        snake_body[0].setheading(270)

def move_left():
    if snake_body[0].heading() != 0:
        snake_body[0].setheading(180)

def move_right():
    if snake_body[0].heading() != 180:
        snake_body[0].setheading(0)

# Listen for key presses
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Creating score board
score = 0
scoreboard = Turtle()
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))

def update_score():
    global score
    score += 1
    scoreboard.clear()  # Clear old score
    scoreboard.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))

# Function to display Game Over and stop game
def game_over():
    scoreboard.goto(0, 0)  # Move the scoreboard to center
    scoreboard.write("Game Over", align="center", font=("Arial", 24, "bold"))
    screen.update()
    time.sleep(2)
    screen.bye()  # Close the game window

# Main game loop
while True:
    screen.update()
    time.sleep(0.1)

    # Move the body (except the head)
    for i in range(len(snake_body) - 1, 0, -1):
        new_x = snake_body[i - 1].xcor()
        new_y = snake_body[i - 1].ycor()
        snake_body[i].goto(new_x, new_y)

    # Move the head forward
    snake_body[0].forward(20)

    # ✅ Detect collision with wall
    if abs(snake_body[0].xcor()) > 290 or abs(snake_body[0].ycor()) > 290:
        game_over()
        break  # Exit loop

    # ✅ Check for food collision
    if snake_body[0].distance(food) < 15:
        update_score()  # Update score
        move_food()  # Move food to a new position

    # ✅ Detect collision with tail (game over)
    for segment in snake_body[1:]:  # Skip head (index 0)
        if snake_body[0].distance(segment) < 10:  # Collision detected
            game_over()
            break  # Exit loop

screen.exitonclick()  # Keep the window open
