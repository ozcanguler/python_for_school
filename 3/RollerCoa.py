print("Welcome to the RollerCoaster")
height=int(input("What is your height in cm?"))
if(height<120):
    print("Sorry, you have to grow taller before you can ride.")
else:
    print("You can ride")
    age=int(input("What is your age?"))
    if(age<12):
        bill=5
        print(f"Child tickets are ${bill}.")
    elif(age<15):
        bill=7
        print(f"Youth tickets are ${bill}.")
    elif(age>=45 and age<=55):
        bill=0
        print("Everything is going to be ok. Have a free ride on us")    
    else:
        bill=12
        print(f"Adult tickets are ${bill}.")        
    wants_photo=input("Do you want a photo taken? Y or N. ")
    if(wants_photo=="Y"):
        bill += 3
        print(f"Your final bill is ${bill}.")
    else:
        print(f"Your final bill is ${bill}.")
