from turtle import Turtle

# Constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        """Initialize the snake body and set the head."""
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]  # The first segment is the head

    def create_snake(self):
        """Creates the initial snake with 3 segments."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Adds a new segment to the snake body."""
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.snake_body.append(segment)

    def extend(self):
        """Extends the snake when it eats food."""
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        """Moves the snake forward."""
        # Move each segment to the position of the previous segment (from tail to head)
        for i in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[i - 1].xcor()
            new_y = self.snake_body[i - 1].ycor()
            self.snake_body[i].goto(new_x, new_y)
        
        self.head.forward(MOVE_DISTANCE)  # Move the head forward

    def move_up(self):
        """Changes direction to UP if not moving DOWN."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        """Changes direction to DOWN if not moving UP."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        """Changes direction to LEFT if not moving RIGHT."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        """Changes direction to RIGHT if not moving LEFT."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
