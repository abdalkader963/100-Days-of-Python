from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine 
# 
menu=Menu()
rep=CoffeeMaker()
money=MoneyMachine()
goal=True
while goal==True:
    order=input(f"What would you like? ({menu.get_items()}):").lower()
    if order == "report":
        rep.report()    
        money.report()
    elif order == "off":
        goal=False    
    else:    
        find=menu.find_drink(order)
        if find != None:
            check_res=rep.is_resource_sufficient(find)
            if check_res == True:
                cost=find.cost
                print(f"It will be {cost}$")
                pay=money.make_payment(cost)
                if pay==True:
                    rep.make_coffee(find)



