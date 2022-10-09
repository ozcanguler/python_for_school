from art import logo
print(logo)
'''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt():   
    before_text=[]
    bbbbb=""
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    while(not direction=="encode" and not direction=="decode"):
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if(direction=="encode"):
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        for i in text:
            for k in range(0,len(alphabet)):
                #if(k not in alphabet):
                    #before_text.append(k)               
                if(i==alphabet[k]):
                    if(k+shift>25):
                        before_text.append(alphabet[k+shift-26])
                    else:    
                        before_text.append(alphabet[k+shift])
            if(i not in alphabet):
                before_text.append(i)               

        print(before_text)
        #for i in before_text:
        #    after_text.append(alphabet[i])
        #print(after_text)
        for i in before_text:
            bbbbb+=i
        print(bbbbb)
        direction_repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
        if(direction_repeat=="yes"):
            encrypt()
        elif(direction_repeat=="no"):
            print("GoodBye!")
            quit()
        else: 
            while(not direction_repeat=="yes" and not direction_repeat=="no"):       
                direction_repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
        if(direction_repeat=="yes"):
            encrypt()
        if(direction_repeat=="no"):
            print("GoodBye!")
            quit()                       
    if(direction=="decode"):
         text = input("Type your message:\n").lower()
         shift = int(input("Type the shift number:\n"))
    for i in text:
        for k in range(0,len(alphabet)):
            #if(k not in alphabet):
                #before_text.append(k)
            if(shift>25):
               shift=shift%26                
            if(i==alphabet[k]):
                if(k-shift>25):
                    before_text.append(alphabet[k-shift-26])
                else:    
                    before_text.append(alphabet[k-shift])
        if(i not in alphabet):
            before_text.append(i)               

    print(before_text)
    #for i in before_text:
    #    after_text.append(alphabet[i])
    #print(after_text)
    for i in before_text:
        bbbbb+=i
    print(bbbbb)
    direction_repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
    while(not direction_repeat=="yes" and not direction_repeat=="no"):
            direction_repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
    if(direction_repeat=="yes"):
        encrypt()
    if(direction_repeat=="no"):
        print("GoodBye!")                   
encrypt()
'''               
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(start_text,shift_amount,cipher_direction):
    end_text=""
    if(cipher_direction=="decode"):
        if(shift_amount>25):
            shift_amount=shift_amount%26
        shift_amount*=-1
    elif(cipher_direction=="encode"):
        if shift_amount>25:
            shift_amount=shift_amount%26
    for letter in start_text:
        if(letter in alphabet):
            position=alphabet.index(letter)       
            new_position=position+shift_amount
            if new_position>25:
                new_position=new_position%26                                            
            end_text+=alphabet[new_position] 
        else:
            end_text+=letter                
    print(f"The {cipher_direction}d text is {end_text}")
should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text,shift,direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")


       
'''          
def encrypt(plain_text,shift_amount):
    cipher_text=""
    for letter in plain_text:
        position=alphabet.index(letter)
        new_position=position+shift_amount
        if(new_position>25):
            new_position=new_position%26   
        new_letter=alphabet[new_position]
        cipher_text+=new_letter
    print(f"The encoded text is {cipher_text}")
#encrypt(text,shift)

def decrypt(plain_text,shift_amount):
    cipher_text=""
    for letter in plain_text:
        position=alphabet.index(letter)
        new_position=position-shift_amount
        if(new_position>25):
            new_position=new_position%26   
        new_letter=alphabet[new_position]
        cipher_text+=new_letter
    print(f"The encoded text is {cipher_text}")

if(direction=="encode"):
    encrypt(text,shift)               
elif(direction=="decode"):
    decrypt(text,shift)
'''     








'''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
  #Try running the program and entering a shift number of 45.
  #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
  #Hint: Think about how you can use the modulus (%).
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")

'''