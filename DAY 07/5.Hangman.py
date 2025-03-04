import random

#todo 1
from hangman_word import word_list
#todo 2
from hangman_art import stages
#todo 3
from hangman_logo import logo


lives = 6
print(logo)

chosen_word = random.choice(word_list).lower()
print(chosen_word)

place_holder = "_" * len(chosen_word)
print(place_holder)

game_over = False
correct_letter = []

while not game_over:

#todo 6
    print(f"*************************************{lives}/6 LIVES LEFT*************************************")
    guess = input("Guess a letter:").lower()

#todo 4
    if guess in correct_letter:
       print(f"you have already gussed {guess}")

    display = ""

    for letter in chosen_word:
      if letter == guess:
         display += letter
         correct_letter.append(guess)
      elif letter in correct_letter:
         display += letter
      else:
         display += "_"
      
    print(display)

#todo 5

    if guess not in chosen_word:
        lives -= 1
        print(f"You gussed {guess},thats not in a word.You loose a life.")
        if lives == 0:
         game_over = True

 #todo 7
        print(f"*************************************IT WAS {chosen_word}! YOU LOOSE*************************************")

    if "_" not in display:
      game_over = True
      print("You win")
      print("*************************************YOU WIN!*************************************")

#todo 2
    print(stages[lives])
  