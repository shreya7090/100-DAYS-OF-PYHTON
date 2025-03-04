import random
word_list = ["baloon","Flower","Camel"]
chosen_word = random.choice(word_list).lower()
print(chosen_word)

place_holder = "_" * len(chosen_word)
print(place_holder)

game_over = False
#todo 2
correct_letter = []

#todo 1
while not game_over:
    guess = input("Guess a letter:").lower()

    display = ""

    for letter in chosen_word:
      if letter == guess:
         display += letter
         #todo 2
         correct_letter.append(guess)
      elif letter in correct_letter:
         display += letter
      else:
         display += "_"
      
    print(display)
 
    if "_" not in display:
      game_over = True
      print("You win")
 