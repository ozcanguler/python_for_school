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
print(MENU["espresso"]["cost"])
tp=0
while True:
    if(resources["coffee"]>17 and resources["water"]>49):
        choose_drink=input("What would you like? (espresso/latte/cappuccino):")
        if(choose_drink=="r"):
            for i in resources:
                print(f"{i}:{resources[i]}{measurement_unit[i]}")

        elif(choose_drink=="e"):
            if resources["water"]>=MENU["espresso"]["ingredients"]["water"] and (resources["coffee"]>=MENU["espresso"]["ingredients"]["coffee"]):       
                print("Please insert coins")
                for i in coins_:
                    coins_[i]=input(f"How many {i}:")
                    tp+=Decimal(i[6:])*Decimal(coins_[i])
                resources["money"]+=MENU["espresso"]["cost"]
                if(tp>MENU["espresso"]["cost"]):
                    tp-=Decimal(MENU["espresso"]["cost"])
                    resources["water"]-=MENU["espresso"]["ingredients"]["water"]
                    resources["coffee"]-=MENU["espresso"]["ingredients"]["coffee"]
                    print(f"Here is {tp}TL in change")
                    tp=0
                else:
                    print("Sorry that's not enough money. Money refunded.")

        elif(choose_drink=="l"):
            if (resources["water"]>=MENU["latte"]["ingredients"]["water"] and resources["coffee"]>=MENU["latte"]["ingredients"]["coffee"] and resources["milk"]>=MENU["latte"]["ingredients"]["milk"]):       
                print("Please insert coins")
                for i in coins_:
                    coins_[i]=input(f"How many {i}:")
                    tp+=Decimal(i[6:])*Decimal(coins_[i])
                resources["money"]+=MENU["latte"]["cost"]
                if(tp>MENU["latte"]["cost"]):
                    tp-=Decimal(MENU["latte"]["cost"])
                    resources["water"]-=MENU["latte"]["ingredients"]["water"]
                    resources["coffee"]-=MENU["latte"]["ingredients"]["coffee"]
                    resources["milk"]-=MENU["latte"]["ingredients"]["milk"]
                    print(f"Here is {tp}TL in change")
                    tp=0
                else:
                    print("Sorry that's not enough money. Money refunded.")

        elif(choose_drink=="c"):
            if (resources["water"]>=MENU["cappuccino"]["ingredients"]["water"] and resources["coffee"]>=MENU["cappuccino"]["ingredients"]["coffee"] and resources["milk"]>=MENU["cappuccino"]["ingredients"]["milk"]):       
                print("Please insert coins")
                for i in coins_:
                    coins_[i]=input(f"How many {i}:")
                    tp+=Decimal(i[6:])*Decimal(coins_[i])
                resources["money"]+=MENU["cappuccino"]["cost"]
                if(tp>MENU["cappuccino"]["cost"]):
                    tp-=Decimal(MENU["cappuccino"]["cost"])
                    resources["water"]-=MENU["cappuccino"]["ingredients"]["water"]
                    resources["coffee"]-=MENU["cappuccino"]["ingredients"]["coffee"]
                    resources["milk"]-=MENU["cappuccino"]["ingredients"]["milk"]
                    print(f"Here is {tp}TL in change")
                    tp=0
                else:
                    print("Sorry that's not enough money. Money refunded.")

    else:
        print("There is no coffee left in the machine")
        break                  