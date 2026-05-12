#Secret Auction System
# first I tryed making it with out dictionary :
goal = False 
name=[]
price=[]
while not goal :
    na=input("What is your name?\n").lower()
    bi=int(input("What is your bid?\n"))
    q=input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    name.append(na)
    price.append(bi)
    if q == "no":
        goal=True
    if q== "yes":
        goal=False
largest_bid=max(price)        
print(largest_bid)
loc=price.index(largest_bid)
na_loc=name[loc]
print(f"The winner is {na_loc} with a bid of {largest_bid}")
#///////////////////////////////////////////////////////////////////////
#after i learnd dictionarys :
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
goal = False
dic={}
while not goal:
    na=input("What is your name?: ").lower()
    bid=int(input(("What is your bid?: $ ")))
    dic[na]=bid
    f=input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if f == "yes":
        clear_screen()
        goal=False
    elif f == "no":
        goal = True
        clear_screen()
winner=max(dic, key=dic.get)   
highest_bid=dic[winner]     
print(f"The winner is {winner} with a bid of ${highest_bid}")  
