import random
import art

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(hand):
    if 11 in hand and 10 in hand and len(hand) == 2:  # Blackjack
        return 0
    if 11 in hand and sum(hand) > 21:  # Adjust Ace if over 21
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def play_game():
    print(art.logo)
    print("WELCOME TO BLACKJACK GAME")
    
    user_cards = [deal_card() for _ in range(2)]
    computer_cards = [deal_card() for _ in range(2)]

    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards} , current score: {user_score}")
        print(f"Computer cards: {computer_cards[0]}")
        
        if computer_score == 0 or user_score == 0 or user_score > 21:
            game_over = True
        else:
            want_to_continue = input("Press 'y' to get another card, type 'n' to pass: ").lower()
            if want_to_continue == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    user_score = calculate_score(user_cards)  # Final user score
    computer_score = calculate_score(computer_cards)  # Final computer score
    
    print(f"Your final cards: {user_cards} , your final score: {user_score}")
    print(f"Computer's final cards: {computer_cards} , computer's final score: {computer_score}")

    return user_score, computer_score  # Return final scores

def compare(user_score, computer_score):
    if user_score == computer_score:
        print("It's a draw.")
    elif user_score > computer_score:
        print("You won!")
    elif user_score < computer_score:
        print("You lost.")
    elif user_score > 21:
        print("You went over 21. You lose.")
    elif computer_score > 21:
        print("Computer went over 21. You win!")
    elif computer_score == 0:
        print("You lose. Computer has a blackjack.")
    elif user_score == 0:
        print("You win with a blackjack!")

# Main game loop
while input("Do you want to play the game BLACKJACK? Type 'yes' to play: ").lower() == 'yes':
    print("\n" * 30)
    user_score, computer_score = play_game()  # Get final scores from play_game()
    compare(user_score, computer_score)  # Compare the scores to decide the winner
