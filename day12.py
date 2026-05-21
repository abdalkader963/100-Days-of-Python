#guessing the number game 
import random
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
def set_diff():
    while True:    
        difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty =="easy":
            return 10
        elif difficulty == "hard":
            return 5   
        print("input error!")
def game():
    global attempts
    number=random.randint(1,100)
    print(f"you have {attempts} remaining to guess the number.")
    while attempts >0:
        guess1=int(input("Make a guess: "))
        if number > guess1:
            attempts -=1
            print(f"too low.\nyou have {attempts} attempts left.")
        elif number == guess1:
            return f"You got it! The answer was {guess1}"    
        else:
            attempts -=1
            print(f"too high.\nyou have {attempts} attempts left.") 
    return "You've run out of guesses."
goal=False
while not goal:
    attempts=set_diff()  
    print(game())
    i=input("do you want to try again? yes or no: ").lower()
    if i=="yes":
        goal=False
        clear_screen()
    else:
        goal=True 
        clear_screen()   


