import random
from turtle import clear
from art import logo
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card

def calculate_scores(cards):

    #if 11 in cards and 10 in cards and len(cards)==2:

    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)      
    return sum(cards)  

def compare(Player_score,Computer_score):
    if Player_score==Computer_score:
        return "Draw"
    elif Computer_score==0:
        return "Lose, computer has Blackjack"
    elif Player_score==0:
        return "Win, with a Blackjack"
    elif Player_score>21:
        return "You went over. You lose"
    elif Computer_score>21:
        return "Computer went over. You win"
    elif Player_score>Computer_score:
        return "You win"
    else:
        return "You lose"
def play_game():
    print(logo)                          
    Player=[]
    Computer=[]
    game_over=False
    for i in range(0,2):
        Player.append(deal_card())
        Computer.append(deal_card())

    while not game_over:
        Player_score=calculate_scores(Player)
        Computer_score=calculate_scores(Computer)

        print(f"Your cards: {Player}, current score: {Player_score}\nComputer's first card: {Computer[0]}")
        if Player_score==0 or Computer_score==0 or Player_score>21:
            game_over=True
        else:
            hit_card=input("Type 'y' to get another card, type 'n' to pass: ")
            if hit_card=="y":
                Player.append(deal_card())
            else:
                game_over=True
    while Computer_score!=0 and Computer_score<17:
        Computer.append(deal_card())
        Computer_score=calculate_scores(Computer)

    print(f"Your final hand: {Player}, final score: {Player_score}\nComputer's final hand: {Computer}, Computer's final score: {Computer_score}")
    print(compare(Player_score,Computer_score))

while input("Do you want to play Blackjack? Type 'y' or 'n': ")=="y":
    clear()
    play_game()