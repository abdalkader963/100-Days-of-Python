#main game
from game_data import data , logo , vs_art
import random 
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print(logo)
def accounts():
    goal=False
    while not goal:
        A=random.choice(data)
        B=random.choice(data)
        if A==B:
            goal=False
        else:
            goal=True
    # compare the followers count
    comp=0
    if A['follower_count'] > B['follower_count']:
        comp+=1
    else:
        comp==0
    return A, B, comp        

def game(score):
        print(f"Compare A: {acc1['name']}, a {acc1['description']}, from {acc1['country']}.\n{vs_art}\nCompare B: {acc2['name']}, a {acc2['description']}, from {acc2['country']}.")
        user=input("Who has more followers? Type 'A' or 'B': ").lower()
        if user=="a" and comp==1:
            score+=1
            clear_screen()
            print(f"You're right! Current score: {score}.")
        elif user=="b" and comp==0:
            score+=1
            clear_screen()
            print(f"You're right! Current score: {score}.")
        else:
            clear_screen()
            print(f"Sorry, that's wrong. Final score: {score}.")  
            return -1
        return score

goal=False
score1=0
while not goal:
    acc1, acc2, comp = accounts()
    f_score=game(score=score1)
    if f_score==-1:
        goal=True
    else:
        score1=f_score    
    

