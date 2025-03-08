from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1 
        self.penup()
        self.hideturtle()
        self.goto(-270, 260)  # Position scoreboard at the top-left corner
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the displayed level."""
        self.clear()  # Clear previous level display
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        """Increases the level and updates the scoreboard."""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Displays 'Game Over' on the screen."""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
