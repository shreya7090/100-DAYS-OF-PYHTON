from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(20)

screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()

'''
FUNCTION AS INPUT
def function_a(something):
    #do this with something
    #then do this
    #finally do this

def fumction_b():
    #do this

function_a(function_b)
'''