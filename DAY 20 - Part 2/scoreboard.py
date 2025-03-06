from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        # Creating the scoreboard
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        """Displays the current score on the screen"""
        self.clear()  # Clear previous score before updating
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Displays 'GAME OVER' message on the screen"""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_scoreboard(self):
        """Increases the score and updates the scoreboard"""
        self.score += 1
        self.update_scoreboard()  # Call update to refresh the score
