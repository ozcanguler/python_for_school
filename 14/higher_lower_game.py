import random
from higher_lower_data import data

current_score=0
laps=3

a=[]
b=[]
def random_number():
    x=random.randint(0,50)
    return x
    #if(a==b):
    #    random_number()
    #else:

def comparing(a,b):  
    for i in data[random_number()].items():
        a.append(i)       
        #print(a)


    print(f"Compare A: {a[0][1]} a {a[2][1]} from {a[3][1]}")
    #print(a[1][1])
    
    for i in data[random_number()].items():
        b.append(i)
        #print(b)
    print(f"Compare B: {b[0][1]} a {b[2][1]} from {b[3][1]}")
    #print(b[1][1])
    if(a[0][1]==b[0][1]):
        comparing(a,b)
    a=a[1][1]
    b=b[1][1]
    



def choose(current_score,laps):      
    while laps>0:
        comparing(a,b)       
        choice=input("Who has more followers? Type 'A' or 'B':").lower()
        if(choice=="a" or choice=="b"):
            laps-=1
            if(choice=="a"):             
                if(a[1][1]>b[1][1]):
                    current_score+=1
                    print(f"You're right! Current Score:{current_score}, remaining lap: {laps}")
                    a.clear()
                    b.clear()
                else:
                    print(f"Sorry, that's wrong. Current Score:{current_score}, remaining lap: {laps}")
                    a.clear()
                    b.clear()
            if(choice=="b"):               
                if(a[1][1]<b[1][1]):
                    current_score+=1
                    print(f"You're right! Current Score:{current_score}, remaining lap: {laps}")
                    a.clear()
                    b.clear()
                else:
                    print(f"Sorry, that's wrong. Current Score:{current_score}, remaining lap: {laps}")
                    a.clear()
                    b.clear()
        else:
            print(f"Please, choose type 'A' or 'B':{current_score}, remaining lap: {laps}")
            choose(current_score,laps)
            return
            

choose(current_score,laps)