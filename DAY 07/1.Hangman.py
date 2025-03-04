import random
#todo 1
word_list = ["baloon","Flower","Camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

#todo 2
guess = input("Guess a letter:").lower()
print(guess)

#todo 3
for letter in chosen_word:
    if letter == guess:
        print("right")
    else:
        print("wrong")