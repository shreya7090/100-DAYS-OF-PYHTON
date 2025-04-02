import os
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.ensure_data_file()  # ✅ Auto-create data.txt if missing
        self.read_file()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def ensure_data_file(self):
        """✅ Check if data.txt exists; create it if not."""
        if not os.path.exists("data.txt"):
            print("⚠️ data.txt not found! Creating new file...")  
            with open("data.txt", "w") as file:
                file.write("0")  # Create file with initial score 0

    def read_file(self):
        """✅ Read high score from data.txt."""
        try:
            with open("data.txt", "r") as file:
                self.high_score = int(file.read().strip() or "0")  
        except Exception as e:
            print(f"❌ Error reading file: {e}")  
            self.high_score = 0  

    def write_file(self):
        """✅ Save high score to data.txt."""
        try:
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))
        except Exception as e:
            print(f"❌ Error writing to file: {e}")  

    def update_scoreboard(self):
        """✅ Update scoreboard display."""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        """✅ Reset score and update high score if needed."""
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_file()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        """✅ Increase score and update scoreboard."""
        self.score += 1
        self.update_scoreboard()
