import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scisors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock,paper,scisors]

user_choice = int(input("waht do you choose? Type 0 for rock, 1 for paper and 2 for scisors"))
print(game_images[user_choice])

computer_choice = random.randint(0,2)
print("computer chose :")
print(game_images[computer_choice])

if user_choice == 0 and computer_choice == 0:
    print("It's a tie")
elif user_choice == 0 and computer_choice == 1:
    print("U loose")
elif user_choice == 0 and computer_choice == 2:
    print("U win")
elif user_choice == 1 and computer_choice == 0:
    print("U win")
elif user_choice == 1 and computer_choice == 1:
    print("It's a tie")
elif user_choice == 1 and computer_choice == 2:
    print("U loose")
elif user_choice == 2 and computer_choice == 0:
    print("U loose")
elif user_choice == 2 and computer_choice == 1:
    print("U win")
elif user_choice == 2 and computer_choice == 2:
    print("U tie")
else:
    print("There is wrong input choose btw 0, 1 or 2")

