import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
print(names)

rnd_name=random.randint(0,len(names)-1)
print(names[rnd_name] +" is going to buy the meal today!")

#rnd_name=random.choice(names)
#print(rnd_name +" is going to buy the meal today!")