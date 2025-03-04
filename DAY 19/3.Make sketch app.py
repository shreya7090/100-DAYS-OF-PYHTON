from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(20)

def move_backward():
    tim.backward(20)

def move_counter_clockwise():
    tim.left(20)

def move_clockwise():
    tim.right(20)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forward,"W")
screen.onkey(move_backward,"S")
screen.onkey(move_counter_clockwise,"A")
screen.onkey(move_clockwise,"D")
screen.onkey(clear,"C")

screen.exitonclick()
