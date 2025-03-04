#passing function into another function
def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

def calculator(n1,n2,func):
    return func(n1,n2)
result = calculator(2,9,add)
print(result)

#calculator is higher order function bcoz it takes another function as input and works with it.
