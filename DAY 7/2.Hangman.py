
import random
word_list = ["baloon","Flower","Camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

#todo 1
place_holder = "_" * len(chosen_word)
print(place_holder)

guess = input("Guess a letter:").lower()

#todo 2
display = ""


for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)


