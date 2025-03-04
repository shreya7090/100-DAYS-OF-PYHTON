'''
while something_is_true:
    #Do something repeatedly
'''


#TASK 1
'''
def turn_right():
   turn_left()
   turn_left()
   turn_left()
   
def cross_box():
   move()
   turn_left()
   move()
   turn_right()
   move()
   turn_right()
   move()
   turn_left()
    
number_of_cross_box = 6
while number_of_cross_box > 0:
    jump()

    number_of_cross_box -= 1
    print(number_of_cross_box)
'''


#TASK 2
'''
def turn_right():
   turn_left()
   turn_left()
   turn_left()
   
def cross_box():
   move()
   turn_left()
   move()
   turn_right()
   move()
   turn_right()
   move()
   turn_left()
    
while not at_goal():
    cross_box()    
'''

#TASK 3
'''
def turn_right():
   turn_left()
   turn_left()
   turn_left()
   
def cross_box():
   move()
   turn_left()
   move()
   turn_right()
   move()
   turn_right()
   move()
   turn_left()
    
while not at_goal():
    if wall_in_front():
       cross_box()
    else:
       move()  
'''


#TASK 4
'''
def turn_right():
   turn_left()
   turn_left()
   turn_left()
   
def cross_box():
   turn_left()
   while wall_on_right():
       move()
   turn_right()
   move()
   turn_right()
   while front_is_clear():
       move()
   turn_left()
    
while not at_goal():
    if wall_in_front():
       cross_box()
    else:
       move()  
'''
