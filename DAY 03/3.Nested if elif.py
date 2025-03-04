'''
Nested if/elif
if conditon:
   if another conditon1:
     do this
   elif another condition2:
     do this
   else:
     do this
else:
  do this
'''
print("Welcome to the rollercoster")
height = int(input("whats your height in cm?"))
if height >= 120:
    print("You can ride")
    age = int(input("whats your age"))
    if age < 12:
      print("Pay $5")
    elif age > 18:
      print("pay $12")
    else:
       print("Pay $7")
else:
   print("You cant ride")