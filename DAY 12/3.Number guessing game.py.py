import random
import art
print(art.logo)
print("WELCOME TO NUMBR GUESSING GAME!!\nI'm thinking of a number btw 1 and 100.")


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(random_number,user_number,turns):
     if random_number == user_number:
        print(f"You won! The answer is {random_number}")
     elif user_number > random_number:
        print("It's too low")
        return turns -1
     elif user_number < random_number:
        print("It's too high")
        return turns -1


def set_difficulty():
    choose = str(input("Chosse a difficulty.Type 'easy' or 'hard':")).lower()
    if choose == 'easy':
       return EASY_LEVEL_TURNS
    elif choose == 'hard':
        return HARD_LEVEL_TURNS
    else:
        print("Incorrect input.")

def game():
      random_number = random.randint(1,101)
      print(f"passst,the correct answer is{random_number}")
      turns = set_difficulty()

      user_number = 0
      while user_number != random_number:
            print(f"You have {turns} attempts to guess.")
            user_number = int(input("guess the number:"))
            turns = check_answer(user_number,random_number,turns)
            if turns == 0:
                print("You'hv ran out of gusses.You lose.")
                return
game()