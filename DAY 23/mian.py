import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()  # Now tracks levels

# Listen for key presses
screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()  # Randomly create cars
    car_manager.move_cars()   # Move all cars left
    
    # Check if player reached the top
    if player.reached_top():
        player.go_to_start()  # Reset player position
        car_manager.level_up()  # Increase car speed
        scoreboard.level_up()   # Increase level and update display
    
    # Check collision with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20:  # Collision detected
            game_is_on = False
            scoreboard.game_over()  # Show "Game Over" message

screen.exitonclick()
