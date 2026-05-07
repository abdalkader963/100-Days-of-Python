#HANG MAN
import random
citys=["tartous","latakia","damascus","homs","aleppo","idlib"]
random_c=random.choice(citys)
# print(random_c)
city=list(random_c)
place_holder=""
lifes=6
for position in range(len(random_c)):
    place_holder+= "_"
print(place_holder) 
user_goal=False
current_letters=[]
while not user_goal:
    user_guess=input("guess a letter\n").lower()
    display=""  
    if user_guess not in city:
            lifes-=1
    elif user_guess in current_letters:
        #  lifes-=1
         print(f"you've already guessed this letter:{ user_guess}")
    for letter in city:
        if user_guess == letter:
            display+= user_guess
            current_letters.append(user_guess)
        elif letter in current_letters:
            display+= letter   
        else:
            display+= "_"           
    print(display)     
    if "_" not in display:
        user_goal=True 
        print("YOU WON!") 
    if lifes==0:
         user_goal=True
         print(("YOU LOST!"))    
    print(f"your remaining lifes is :{lifes}")    