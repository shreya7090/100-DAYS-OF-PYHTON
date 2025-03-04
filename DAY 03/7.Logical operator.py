'''
if condition1 & condition2 & condition3:
    do this
else:
    do this
'''

'''
A and B 
tt = t
tf = f
ft = f
ff = f

C or D
tt = t
tf = t
ft = t
ff = f

not E
t = f
f = t
'''

print("Welcome to the rollercoster")
height = int(input("whats your height in cm?"))
bill = 0

if height >= 120:
    print("You can ride")

    age = int(input("whats your age"))
    if age < 12:
      print("Child ticket $5")
      bill = 5
    elif age > 18:
      print("Youth ticket $12")
      bill = 12
    elif age >= 45 and age <= 55:
   #elif 45 <= age <= 55:
       print("have a free ride on us!!")
    else:
       print("Adult ticket $7")
       bill = 7

    picture = str(input("Do you want picture? Type Y for yes and N for No")).upper()
    if picture == "Y":
       print("Pay $3")
       bill += 3

    print(f"Your final bill is ${bill}")
else:
   print("You cant ride")
