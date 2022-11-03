from decimal import *
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money":0
}
measurement_unit = {
    "water": "ml",
    "milk": "ml",
    "coffee": "gr",
    "money": "TL",} 

coins_ = {
    "coins_0.25": 0,
    "coins_0.50": 0,
    "coins_1.00": 0,}
tp=0
choose_drink=input("What would you like? (espresso/latte/cappuccino):")
if(choose_drink=="r"):
    for i in resources:
        print(f"{i}:{resources[i]}{measurement_unit[i]}")
elif(choose_drink=="e"):
    print("Please insert coins")
    for i in coins_:
        coins_[i]=input(f"How many {i}:")
        tp+=Decimal(i[6:])*Decimal(coins_[i])
    print(tp)                 