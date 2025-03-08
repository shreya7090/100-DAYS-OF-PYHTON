from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90
DOWN = 270

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        """Moves the turtle forward when Up key is pressed."""
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """Moves the player back to the starting position."""
        self.goto(STARTING_POSITION)

    def reached_top(self):
        """Returns True if the player reached the top edge."""
        return self.ycor() > FINISH_LINE_Y
