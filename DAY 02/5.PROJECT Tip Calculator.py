#The Tip Calculator
print("Welcome to the tip calculator!")
bill = float(input("What is the total bill amount?$"))
tip = int(input("How much tip would you like to give? 10 12 15"))
split = int(input("How many people to split the bill?:"))

tip_as_percentage = tip/100 
total_tip_amount = bill * tip_as_percentage
total_bill = bill + total_tip_amount 
bill_per_person = total_bill / split
total_amount = bill_per_person
print(f"Your total amount is:${total_amount}")

total = ((((bill * (tip / 100)) + bill) / split))
print(total)

total = ("{:.2f}".format((((bill * (tip / 100)) + bill) / split)))
print(total)
#The "{:.2f}".format(...) part is used to format the final result to two decimal places.
#"{:.2f}" ensures that the result is rounded to two decimal places, which is typical for currency.
