choice=(input("Do you want get in roller coaster?\n true or false\n"))
if choice=="true":

    age=int(input("What is your age?"))
    if age>=18:
       print("Please pay $12.")
    elif age>12:
       print("Please pay $7.") 
    else:
       print("Please pay $5.")
else:
    print("Have a nice day")           