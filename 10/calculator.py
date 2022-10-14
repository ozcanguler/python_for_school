def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def multi(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2 
opera={
"+":add,
"-":sub,
"*":multi,
"/":div
}  
def cal():
    opera_control=False     
    n1=float(input("Enter the firstNumber\n"))


    for key in opera:
        print(key)
    while not opera_control:
        op=(input("Pic an operation: "))
        if op=="+" or op=="-" or op=="*" or op=="/":
            opera_control=True    
    n2=float(input("Enter the secondNumber\n"))
    result=opera[op](n1,n2)
    print(f"{n1}{op}{n2}={result}")

    while opera_control:
        con=input(f"Type 'y' continue calculating with {result},or type 'n' to start a new calculation or type 'e' to exit: ")
        if con=="y" or con=="n" or con=="e":
            if con=="y":
                opera_control=False
                op=input("Pic an operation: ")
                if op=="+" or op=="-" or op=="*" or op=="/":
                    n3=float(input("Enter the nextNumber\n"))
                    result2=opera[op](result,n3)
                    print(f"{result}{op}{n3}={result2}")
                    result=result2
                    opera_control=True
                else:
                    opera_control=True
            if con=="e":
                print("Adiós")
                opera_control=False
            if con=="n":
                cal()
                opera_control=False
cal()

'''
while not opera_control:
    op=input("Pic an operation: ")
    if op=="+" or op=="-" or op=="*" or op=="/":
        opera_control=True
        n3=int(input("Enter the nextNumber\n"))
        result2=opera[op](result,n3)
        print(f"{result}{op}{n3}={result2}")
        result=result2
        opera_control=False  
'''