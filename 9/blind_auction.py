import os
from art import logo
print(logo)
clear = lambda: os.system('cls')
print("Welcome to the secret auction program")


attendants = {}

bidding_finished=False

def highest_record(bidding_record):
    highest_bid=0
    winner=""
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name=input("What's your name?")
    bid=int(input("What's your bid? $"))
    attendants[name]=bid
    should_continue=input("Are there any other bidders? Type 'yes or 'no'.")
    if should_continue=="no":
        bidding_finished=True
        highest_record(attendants)
    elif should_continue=="yes":
        clear()   
