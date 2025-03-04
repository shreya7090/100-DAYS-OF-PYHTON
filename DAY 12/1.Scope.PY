#Local scope :Variables defined outside of any function or block.
x = 10  
def show_x():
    print(x) 
show_x()

#Global scope :Variables defined inside a function
def my_function():
    y = 10
    print(y)
my_function()  

