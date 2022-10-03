import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letters_selected=[]
letters_symbols=[]
letters_numbers=[]
for i in range(0,nr_letters):
    letters_selected.append(letters[random.randint(0,len(letters)-1)])
print(letters_selected)
#for i in letters_selected:
#    print(i)
for j in range(0,nr_symbols):
    letters_symbols.append(numbers[random.randint(0,len(numbers)-1)])
print(letters_symbols)
for k in range(0,nr_numbers):
    letters_numbers.append(symbols[random.randint(0,len(symbols)-1)])
print(letters_numbers)
myPassword=letters_selected+letters_symbols+letters_numbers
#print(len(myPassword))
#print(myPassword)
new_password_selected=[]

for z in range(len(myPassword)):
    if(len(myPassword)>=0):
        k=random.randint(0,len(myPassword)-1)
        new_password_selected.append(myPassword[k])
        myPassword.remove(myPassword[k])
           
print(new_password_selected)
mynewpassword=""
for tt in new_password_selected:
    mynewpassword=mynewpassword+tt
print(mynewpassword)
''' ***************MY TEST CODE *********************
letters_selected=['1','2','3','4','5']
new_letters_selected=[]
for z in range(5):
    if(len(letters_selected)>=0):
        k=random.randint(0,len(letters_selected)-1)
        new_letters_selected.append(letters_selected[k])
        letters_selected.remove(letters_selected[k])
           
#print(letters_selected[0])
print(new_letters_selected)

****************************************************
'''

''' ***************SECOND CODE *********************
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []
for char in range(1,nr_letters+1):
    password_list.append(random.choice(letters))

for char in range(1,nr_symbols+1):
    password_list += random.choice(symbols)

for char in range(1,nr_numbers+1):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char    
print(f"Your password is: {password}")    
****************************************************
'''