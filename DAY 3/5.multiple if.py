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
