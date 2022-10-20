from mimetypes import guess_type
from random import randint

'''
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

'''
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5


def check_answer(guess,answer,turns):
    ''' checks answer against guess. Returns the number of turns remaining'''
    if guess>answer:
        print("Too high.")
        return turns-1
    elif guess<answer:
        print("Too low.")
        return turns-1
    else:
        print(f"You got it! The answer was {answer}.")
def set_difficulty():
    level=input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level=="easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
def game():
    print("Welcome to the number guessing game\nI'm thinking of a number between 1 and 100.")
    answer=randint(1,100)
    print(f"The correct answer is {answer}")

    turns=set_difficulty()
    

    guess=0
    while guess!=answer:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess:"))
        turns=check_answer(guess,answer,turns)
        if turns==0:
            print("You've run out of guesses, you lose.")
            return
        elif guess!=answer:
            print("Guess again")
game()
