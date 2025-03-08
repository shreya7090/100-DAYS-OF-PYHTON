from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE  # Added: Store current speed

    def create_car(self):
        """Creates a new car randomly."""
        #random chance bcoz it creates less cars at a time.
        random_chance = random.randint(1, 6)
        if random_chance == 1:  # Creates a car only sometimes to avoid overcrowding
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # Make car wider
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))  # Random y-position, right edge
            self.all_cars.append(new_car)

    def move_cars(self):
        """Moves all cars left."""
        for car in self.all_cars:
            car.backward(self.car_speed) 

    def level_up(self):
        """Increases car speed when level increases."""
        self.car_speed += MOVE_INCREMENT  
