import art
print(art.logo)

print("Welcome to secrete auction program")

def find_highest_bidder(bidding_dict):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"Winner is {winner} with a bid of $ {highest_bid}")



bids = {}
countinue_bidding = True
while countinue_bidding:
    name = (input("what is your name?\n"))
    price = (int(input("Whats your bid\n$")))
    bids[name] = price
    should_countinue = input("Is there any other users who want to bid? Type 'yes' or 'no'\n").lower()
    if should_countinue == "no":
        countinue_bidding = False
        find_highest_bidder(bids)
    elif should_countinue == "yes":
        print("\n"*80)


