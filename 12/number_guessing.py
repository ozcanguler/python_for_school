from random import randint


print("Welcome to the number guessing game\n I'm thinking of a number between 1 and 100.")

def make_guess(guess_count,number):
    if(guess_count>0):
        guess=int(input("Make a guess: "))
        if(guess==number):
            print("You Win")
        elif(guess>number):
            guess_count-=1
            print(f"High\nGuess again\nYou have {guess_count} attempts remaining to guess the number")
            make_guess(guess_count,number)           
        elif(guess<number):
            guess_count-=1
            print(f"Low\nGuess again\nYou have {guess_count} attempts remaining to guess the number")
            make_guess(guess_count,number)            
    else:
        print("You lost")




def choose_level():
    number=randint(0,100)
    difficult=input("Choose a difficulty. Type 'easy' or 'hard': ")
    if(difficult=="easy"):
        guess_count=10
        make_guess(guess_count,number)
    elif(difficult=="hard"):
        guess_count=5
        make_guess(guess_count,number)
    else:
        choose_level()

choose_level()