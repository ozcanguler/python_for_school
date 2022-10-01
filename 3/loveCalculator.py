print("Welcome to the Love Calculator!")
name1=input("What is your name?\n")
name2=input("What is their name?\n")
name1_lower=name1.lower()
name2_lower=name2.lower()

total_names=name1_lower+name2_lower
true_count=total_names.count("t")+total_names.count("r")+total_names.count("u")+total_names.count("e")

love_count=total_names.count("l")+total_names.count("o")+total_names.count("v")+total_names.count("e")


print(true_count)
print(love_count)

#num_int=int(str(true_count)+str(love_count))
num_str=str(true_count)+str(love_count)
num_int=int(num_str)
if(num_int<10 or num_int>90):
    print(f"Your score is {num_int}, you go together like coke and mentos.")
elif(num_int>40 and num_int<50):
    print(f"Your score is {num_int}, you are alright together.") 
else:
    print(f"Your score is {num_int}.")     
#print(num_int)
#print(num_str+" %")

