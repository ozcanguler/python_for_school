from tkinter import OUTSIDE


apple=1
def increase_apples():
    apple=2
    print(f"inside function: {apple}")
increase_apples()
print(f"outside function: {apple}")


game_level=5
def fruits():
    fruits=["grape","banana","pineapple"]
    if game_level>2:
        new_fruit=fruits[0]
    print(new_fruit)
fruits()

number=2
num=2
nn=2
def increase_numbers():
    number=222
    print(f"numbers inside function: {number}")
    global num
    num+=1
    return num+4
increase_numbers()
print(f"numbers outside function: {number}")
print(f"num outside function: {num}")
print(f"nn outside function: {nn}")
print(increase_numbers())