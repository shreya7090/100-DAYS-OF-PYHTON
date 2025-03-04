print("welcome to python pizza deliveries!!")
bill = 0

size = str(input("What size do you want? S, M, or L:")).upper()
if size == "S":
  print("Small pizza is $15")
  bill = 15
elif size == "M":
  print("Medium pizza is $20")
  bill = 20
elif size == "L":
  print("Large pizza $25")
  bill = 25
else:
  print("You typed the wrong inputs")

pepperoni = str(input("Do you want pepperoni? Y or N:")).upper()
if pepperoni == "Y":
  print("Do you want S, M, or L?")
  if pepperoni == "S":
    print("Small pepperoni is $2")
    bill += 2
  elif pepperoni == "M" or "L":
    print("Medium and Large pepperoni are $3")
    bill += 3

extra_cheese = str(input("Do you want extra cheese? Y or N:"))
if extra_cheese == "Y":
  print("Extra cheeze is $1")
  bill += 1
else:
  print("okay")

print(f"Your total bill is {bill}")
