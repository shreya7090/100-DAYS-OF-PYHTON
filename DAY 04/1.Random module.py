#https://docs.python.org/3/library/random.html

import random
#for integer
random_integer = random.randint(0,19)
print(random_integer)
#for float
random_float = random.random() 
print(random_float)

random_uniform = random.uniform(0,11)
print(random_uniform)

#Heads or tail
game = random.choice(["heads","tails"])
print(game)
