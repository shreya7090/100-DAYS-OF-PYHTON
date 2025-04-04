from turtle import Turtle,Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=700,height=500)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter the colour: ")
colors = ["red","green",'blue',"orange","yellow","purple"]
print(user_bet)
y_positions = [-130, -80, -30, 20, 70, 120]
all_turtle = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-310,y = y_positions[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 315:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)


screen.exitonclick()