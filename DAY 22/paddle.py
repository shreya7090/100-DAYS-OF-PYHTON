from turtle import Turtle,Screen
screen = Screen()

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.move_speed = 20  # Speed of movement
        self.moving_up = False
        self.moving_down = False

    def move_up(self):
        """Continuously moves the paddle up when key is held."""
        if self.moving_up and self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + self.move_speed)
            screen.ontimer(self.move_up, 50)  # Calls itself repeatedly

    def move_down(self):
        """Continuously moves the paddle down when key is held."""
        if self.moving_down and self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() - self.move_speed)
            screen.ontimer(self.move_down, 50)  # Calls itself repeatedly

    def go_up(self):
        self.moving_up = True
        self.move_up()

    def stop_up(self):
        self.moving_up = False

    def go_down(self):
        self.moving_down = True
        self.move_down()

    def stop_down(self):
        self.moving_down = False
