#
from project_data import MENU, COIN_VALUES
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

resources={
    "water":300,
    "milk":200,
    "coffee":100,
    "money":0
}
def get_user_choice():
    while True:
        try:
            inn= input("What would you like?\n(espresso, latte, cappuccino): ").lower()
            if inn in MENU:
                return inn
            elif inn == "off" or inn== "report":
                return inn
            else:
                raise KeyError
        except KeyError:
            print("Pleas choose an item from the Menu.")


def start_machine(user_in):
        # clear_screen()
        if user_in == "off":
            print("Turning off the machine...")    
            return False      
        elif user_in == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${resources['money']}")
            return "report"
        else:
            print(f"Preparing to make {user_in}...")
            return user_in


def changes(user_in):
    if user_in=="report":
        return True
    resources["water"]=resources["water"]-MENU[user_in]["ingredients"]["water"]
    resources["milk"]=resources["milk"]-MENU[user_in]["ingredients"]["milk"]
    resources["coffee"]=resources["coffee"]-MENU[user_in]["ingredients"]["coffee"]
    return resources

def prices(user_in):
    if user_in=="report":
        return True    
    while True:
        try:
            print("pleas insert coins.")
            qua=int(input("how many quarters: "))
            dim=int(input("how many dimes: "))
            nic=int(input("how many nickels: "))
            pen=int(input("how many pennies: "))        
            total= COIN_VALUES["quarters"]*qua +  COIN_VALUES["dimes"]*dim+ COIN_VALUES["nickels"]*nic+ COIN_VALUES["pennies"]*pen
            total_in=(total)
            user_bill=MENU[user_in]["price"]
            resources["money"]+=user_bill
            if total_in< user_bill:
                print("Sorry thats not enough money, money refunded.")
                return True
            elif total_in== user_bill:
                print(f"Here is your {user_in} enjoy")   
                return True
            else:
                final_bill=float(total_in-user_bill)
                print(f"\nHere is {final_bill:.2f} in change.")
                print(f"\nHere is your {user_in} enjoy")  
                return True
        except ValueError:
            True 

def check_resources(user_in):
    if user_in=="off":
        return "off"
    if user_in=="report":
        return "report"
    for res in MENU[user_in]["ingredients"]:
        r1=MENU[user_in]["ingredients"][res]
        r2=resources[res]
        if r2>=r1:
            return True
        else:
            missing_item.append(res)
            return False

while True:
    user_drink=get_user_choice()
    missing_item=[]
    storage=check_resources(user_in=user_drink)
    if storage== False:
        print(f"Sorry,{missing_item[0]} is missing!")
        break
    if storage== "report":
        pass
    if storage == "off":
        print("Turning off the machine...")
        break
    machine=start_machine(user_in=user_drink)
    if machine == False:
         break
    elif machine== "report":
        True
    else:    
        prices(user_in=user_drink)    
        new=changes(user_in=machine)
