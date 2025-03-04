from turtle import Turtle,Screen

screen = Screen()
screen.setup(width=700,height=500)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter the colour: ")
colors = ["red","green",'blue',"orange","yellow","purple"]
print(user_bet)


for turtle_index in range(0,6):
    tim = Turtle(shape = "turtle")
    tim.penup()
    tim.goto(x=-310,y=-150)





screen.exitonclick()