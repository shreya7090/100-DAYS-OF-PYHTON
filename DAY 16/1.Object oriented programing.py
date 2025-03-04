'''
waiter(OBJECT) - HAS(Attributes): is_holding_plate = True
         tables_responsible = [4,5,6]
         -Attritubets are modeled by Variables

         DOES(Methods): def take_order(table,order):
                   #takes order to chef
               def take_payments(amount):
                   #add money to restaurant
        -Methods are modeled by Functions

CLASS - OBJECT
from object class we can generate as many objects as we want.
car       =      CarBlueprint()
object           class
'''

from turtle import Turtle, Screen
#object = class
timmy = Turtle()

print(timmy)
timmy.shape("turtle")
timmy.color("green")
timmy.forward(100)
#object.callmethod

my_screen = Screen()
print(my_screen.canvheight)
#print(object_name.attribute)
#screen is object and canvaheight is attribute that associated with screen.

my_screen.exitonclick()