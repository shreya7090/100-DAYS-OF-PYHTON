import game_data
import art
import random
print(art.logo)

def play_game(score = 0): 

    choose1,choose2 = random.sample(game_data.data,2)
     
    print(f"Compare A:{choose1['name']}, {choose1['description']}, {choose1['country']}")
    print(art.vs)
    print(f"Against B:{choose2['name']}, {choose2['description']}, {choose2['country']}")

    while True:
        user_choose = input("Who has more followers? Type 'A' OR 'B':").lower()
        if user_choose in ['a','b']:
          break
        else:
          print("Invalid input. Please type 'A' or 'B'.")

    if choose1['follower_count'] > choose2['follower_count']:
        correct_answer = 'a'
    else:
        correct_answer = 'b'
    
    if user_choose == correct_answer:
      score += 1
      print(f"You're right! Current score:{score}")
      play_game(score)
    else:
        print(f"You lose.Final score:{score}\nGAME OVER")
play_game()

