import random
from hang_module import hang,word_list
print(hang)
'''
#word_list="space","rocket","earth","gagarin"
#word=random.randint(0,len(word_list)-1)
word="gagarin"
my_guess=[]
#print(word_list[word])
for letter in word:
    my_guess.append("_")
print(my_guess)
while(my_guess.count("_")>0):
    letter=input("Guess a letter:").lower()
    
    #for i in range(0,len(word)):       
    #    if(letter.lower()==word[i]):
     #       print("Right")
     #   else:
     #       print("Wrong")
    
    for i in range(0,len(word)):        
        if(letter==word[i]):
            my_guess[i]=letter
            print("Right")
        else:
            print("Fal")  
    print(my_guess)
print("You Win") 

'''
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
stage=7


print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You have already guessed {guess}")    
        #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
   


    print(f"{' '.join(display)}")
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        stage=stage-1
        print(stages[stage])
       
    if "_" not in display:
        end_of_game = True
        print("You win.")
    if stage==0:
       end_of_game = True
       print("You lost.")

'''
print(logo)
game_is_finished = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    guess = input("Guess a letter: ").lower()

    #Use the clear() function imported from replit to clear the output between guesses.
    clear()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose.")
    
    if not "_" in display:
        game_is_finished = True
        print("You win.")

    print(stages[lives])
'''