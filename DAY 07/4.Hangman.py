stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

import random
word_list = ["baloon","Flower","Camel"]

#todo 1
lives = 6

chosen_word = random.choice(word_list).lower()
print(chosen_word)

place_holder = "_" * len(chosen_word)
print(place_holder)

game_over = False
correct_letter = []

while not game_over:
    guess = input("Guess a letter:").lower()

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

#todo 2
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
         game_over = True

 
    if "_" not in display:
      game_over = True
      print("You win")

#todo 3
    print(stages[lives])
