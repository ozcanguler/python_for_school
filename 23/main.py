#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
names=[]
with open("/Users/Garavel/Desktop/pythonsil/ORWFiles/Input/Letters/starting_letter.txt",mode="r") as fileread_letter:
    starting_letter=fileread_letter.read()
    print(starting_letter)
    
    with open("/Users/Garavel/Desktop/pythonsil/ORWFiles/Input/Names/invited_names.txt",mode="r") as fileread_names:
        invited_names=fileread_names.readlines()
        print(invited_names)
        for name in invited_names:
            stripped_name=name.strip()
            names=starting_letter.replace("[name]",stripped_name)
            with open(f"/Users/Garavel/Desktop/pythonsil/ORWFiles/Output/ReadyToSend/letter_for_{stripped_name}.txt",mode="w") as filewrite:
                filewrite.write(names)
        #fileread_letter.close()
    