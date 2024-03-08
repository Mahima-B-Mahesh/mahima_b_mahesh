from replit import clear
from arts import logo

name_dict = {}
print(logo)

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}") 
while True:
    name = input("Enter your name? ")
    bid = int(input("How much price you want to bid? $"))

    name_dict[name] = bid

    decision = input("Enter 'yes' if other users want to bid. Else enter 'no'.  ")
    if decision.lower() == "yes":
        clear()
        continue
    elif decision.lower() == "no":
        exit(find_highest_bidder(name_dict))
