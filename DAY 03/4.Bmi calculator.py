weight = int(input("enter you weight"))
height = float(input("enter your height"))

bmi = weight / (height**2)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normalweight")
else:
    print("Overweight")