#TYPE 1
def is_prime(number):
    if number < 2:
          return False
    for i in range(2,int(number ** 0.5)+ 1):
        if number % i == 0:
             return False
    else:
         return True

#TYPE 2(Angela)
def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False
 
    # Loop through all the numbers between 2 and the number
    for i in range(2, num):
        # Check if the number (num) can be divided by the potential prime number
        if num % i == 0:
            return False
 
    # this return is outside the for loop which will only run once the loop finishes and none of the numbers are divisible. Therefore it is prime.
    return True


