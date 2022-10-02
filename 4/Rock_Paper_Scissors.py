import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
your_chose=int(input("What do you chose? Type 0 for Rock, type 1 for Paper, type 2 for Scissors"))
if(your_chose>=3 or your_chose<0):
    print("You typed an invalid number, you lose!")
else:
    computer_chose=random.randint(0,2)
    list_chose=[rock,paper,scissors]
    print(list_chose[your_chose]+f"\n Computer chose:\n{list_chose[computer_chose]}")

    if(your_chose==0 and computer_chose==0 or your_chose==1 and computer_chose==1 or your_chose==2 and computer_chose==2):
        print("Draw")
    elif(your_chose==0 and computer_chose==1 or your_chose==1 and computer_chose==2 or your_chose==2 and computer_chose==0):
        print("You Lost")
    else:
        print("You Win")