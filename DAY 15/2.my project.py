ask_coffee = input("What would you like? (espresso/latte/cappuccino):").lower()

if ask_coffee in ['espresso','latte','cappuccino']:
    game_on = True
else:
    game_on = False
    print("Invalid Input") 
    pass

if ask_coffee == 'espresso':
    print("Espresso cost's: ₹250")
elif ask_coffee == 'latte':
    print("latte cost's: ₹380")
elif ask_coffee == 'cappuccino':
    print("cappuccino cost's: ₹430")

while game_on:  
    def change():

        user_50_notes = int(input("please insert notes.\nhow many 💰50 notes?:"))
        user_100_notes = int(input("how many 💰100 notes?:"))
        user_200_notes = int(input("how many 💰200 notes?:"))
        user_500_notes = int(input("how many 💰500 notes?:")) 

        _50_notes = 50 * user_50_notes
        _100_notes = 100 * user_100_notes
        _200_notes = 200 * user_200_notes
        _500_notes_ = 500 * user_500_notes
        money = _50_notes + _100_notes + _200_notes + _500_notes_
        
        if ask_coffee == 'espresso':
            cost_esp = 250
            if cost_esp <= money:
                    money -= cost_esp
                    print("Here is your Espresso🍵 Enjoy!")
                    return money
            else:
                return None
            
        elif ask_coffee == 'latte':
            cost_lat = 380
            if cost_lat <= money:
                    money -= cost_lat
                    print("Here is your Latte🍵 Enjoy!")
                    return money
            else:
                return None
            
        elif ask_coffee == 'cappuccino':
            cost_cap = 430
            if cost_cap <= money:
                    money -= cost_cap
                    print("Here is your Cappuccino🍵 Enjoy!")
                    return money
            else:
                return None

    result = change()
        
    if result == 0:
        print("Thank you!")
    elif result is None:
        print("Insufficient money!")
    else:
        print(f"Here is ₹{result} your change\nThank you!")
        

    
