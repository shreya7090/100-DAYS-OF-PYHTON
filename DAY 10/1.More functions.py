'''
FUNCTIONS
def my_function():
    #Do this
    #then do this
    #finally do this

my_function()
'''

'''
FUNCTIONS WITH INPUTS
def my_function(something):
    #Do this something
    #then do this
    #finally do this

my_function()
'''

'''
FUNCTIONS WITH OUTPUTS
def my_function():
    result = 2 * 4
    return result

output = my_function()
'''

def format_name(f_name,l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return(f"{formated_f_name} {formated_l_name}")

print(format_name(f_name="shreya",l_name="patil"))

