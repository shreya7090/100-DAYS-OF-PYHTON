print("Welcome to Treasure Island\n Your mission is to find the treasure.")
crossroad =  input("You're at the crossroad where do you want to go? Type 'left' or 'right").lower()
if crossroad == 'left':
    s_w = input('Want to swim or wait for a boat? Type "swim" or "wait"').lower()
    if s_w == 'wait':
        door = input('You\'hv arrived at the island.Which door you want to choose? type "Red" "Yellow" or "Blue"').lower()
        if door == "red":
            print("Room of fire.\nGAME OVER")
        elif door == "blue":
            print("YOU WIN")
        elif door == "yellow":
            print("You got attacked by shreya.GAME OVER")
    else:
        print("GAME OVER")
else:
    print("Game over")