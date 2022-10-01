print("Welcome to Python Pizza Deliveries")
size=input("What size pizza do you want? S,M,L\n")
add_pepperoni=input("Do you want pepperoni? Y,N\n")
extra_cheese=input("Do you want extra cheese? Y,N\n")
if(size=="S"):
    price=15
    if(add_pepperoni=="Y"):
        price+=2
        if(extra_cheese=="Y"):
            price+=1

if size=="M":
    price=20
    if(add_pepperoni=="Y"):
        price+=3
        if(extra_cheese=="Y"):
            price+=1

if size=="L":
    price=25
    if(add_pepperoni=="Y"):
        price+=3
        if(extra_cheese=="Y"):
            price+=1
print(f"Your final bill is: ${price}")       



print("Welcome to Python Pizza Deliveries")
size=input("What size pizza do you want? S,M,L\n")
add_pepperoni=input("Do you want pepperoni? Y,N\n")
extra_cheese=input("Do you want extra cheese? Y,N\n")
if(size=="S"):
    price=15
elif(size=="M"):
    price=20
else:
    price=25

if(add_pepperoni=="Y"):
    if size=="S":
        price+=2
    else:
        price+=3
       
if(extra_cheese=="Y"):
    price+=1   
print(f"Your final bill is: ${price}")    