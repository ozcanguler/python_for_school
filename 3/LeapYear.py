
year=int(input("Which year do you want to check?"))
if year%4==0:
    if(year%400==0):
        print(f"So the year {year} is a leap year.")
    elif(year%100==0):
        print(f"So the year {year} is a not leap year.")
    else:
        print(f"So the year {year} is a leap year.")    
else:
    print(f"So the year {year} is a not leap year.")          



year=int(input("Which year do you want to check?"))
if year%4==0:
    if(year%100==0):
        if(year%400==0):
            print(f"So the year {year} is a leap year.")    
        else:
            print(f"So the year {year} is a not leap year.")          
    else:
       print(f"So the year {year} is a leap year.")
else:
   print(f"So the year {year} is a not leap year.")          
