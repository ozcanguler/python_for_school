
#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from random import randint


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
Player=[]
Computer=[]
sum_player=0
sum_computer=0
should_continue=True
should_continue1=True

for i in range(0,2):
    Player.append(cards[randint(0,len(cards)-1)])
    Computer.append(cards[randint(0,len(cards)-1)])
    sum_player=sum(Player)
    sum_computer=sum(Computer)   
print(f"Your cards: {Player}, current score: {sum_player}\nComputer's first card: {Computer[0]}")

while should_continue:
    hit_card=input("Type 'y' to get another card, type 'n' to pass: ")
    if hit_card=="y":
        Player.append(cards[randint(0,len(cards)-1)])
        sum_player=sum(Player)
        sum_computer=sum(Computer)
        if sum_computer<21 and sum_computer<sum_player:
            Computer.append(cards[randint(0,len(cards)-1)])
            sum_computer=sum(Computer)
    '''
    if hit_card=="n":       
        if(sum_computer>21):
            print("You Win")
            should_continue=False    
        elif(sum_computer>sum_player):
            print("You lost")
            should_continue=False    
        elif sum_computer<21 and sum_computer<sum_player:
            Computer.append(cards[randint(0,len(cards)-1)])
            sum_computer=sum(Computer)             
        elif sum_player == sum_computer:
            print("Draw")
            should_continue=False
            '''    
    print(f"Your final hand: {Player}, final score: {sum_player}\nComputer's final hand: {Computer}, final score: {sum_computer}")
    if(sum_computer>21):
        print("You Win")
        should_continue=False    
    elif(sum_player<21 and sum_player<sum_computer):
        should_continue:True              
    elif(sum_computer>sum_player and sum_computer<22):
        print("You lost")
        should_continue=False
    elif(sum_player>21):
        print("You lost")
        should_continue=False
    elif(sum_computer>21 and sum_player<22):
        print("You Win")
        should_continue=False    
    elif(sum_player>sum_computer):
        if(sum_computer<21):
            while sum_computer<sum_player and sum_computer<21:
                Computer.append(cards[randint(0,len(cards)-1)])
                sum_computer=sum(Computer)
                print(f"Your final hand: {Player}, final score: {sum_player}\nComputer's final hand: {Computer}, final score: {sum_computer}")
                if(sum_player>sum_computer or sum_computer>21):
                    print("You Win")
                    should_continue=False
                elif(sum_player==sum_computer):
                    print("Draw")
                    should_continue=False   
                else:
                    print("You lost")
                    should_continue=False
        elif(sum_player>sum_computer):
            print("You Win")
            should_continue=False
        else:
            print("You lost")
            should_continue=False
    elif(sum_player==sum_computer and sum_player<21):
        should_continue=True
    elif(sum_player==sum_computer):
        print("Draw")
        should_continue=False
    '''
    elif hit_card=="n":
        should_continue=False
        while sum_computer<=sum_player:                                                    
            if sum_computer<=sum_player:
                Computer.append(cards[randint(0,len(cards)-1)])
                sum_computer=sum(Computer)
                should_continue1=True
                should_continue=False
                print(f"Your final hand: {Player}, final score: {sum_player}\nComputer's final hand: {Computer}, final score: {sum_computer}")
            elif sum_computer>sum_player:
                should_continue=False
                if(sum_computer>21):
                    #print("You Win") 
                    should_continue1=False
                    should_continue=False                    
                elif(sum_computer>sum_player):
                    #print("You lost")
                    should_continue1=False
                    should_continue=False 
                elif sum_player == sum_computer and sum_computer>20:
                    should_continue1=False
                    should_continue=False
                    #print("Draw")
    '''                                               

    if hit_card=="n":
        should_continue=False
        if sum_computer<=sum_player and sum_computer<22:
            print("kucuk")
        else:
            print("You lost")




            #print(f"Your final hand: {Player}, final score: {sum_player}\nComputer's final hand: {Computer}, final score: {sum_computer}")