#Rock Paper Scissors
import random
game= ["paper" , "rock" , "scissors"] 
bot_play=random.choice(game)
player_play=input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
if player_play=="0":
    print("you played 'rock'")
    if bot_play=="rock":
        print("bot played 'rock'")
        print("TIE!")
    elif bot_play=="paper":
        print("bot played 'paper'")
        print("YOU LOST!")
    elif bot_play=="scissors":
        print("bot played 'scissors'")
        print("YOU WON!")
elif player_play=="1":
    print("you played 'paper'")
    if bot_play=="rock":
        print("bot played 'rock'")
        print("YOU WON!")
    elif bot_play=="paper":
        print("bot played 'paper'")
        print("TIE!")
    elif bot_play=="scissors":
        print("bot played 'scissors'")
        print("YOU LOST!")        
elif player_play=="2":
    print("you played 'SCISSORS'")
    if bot_play=="rock":
        print("bot played 'rock'")
        print("YOU LOST!")
    elif bot_play=="paper":
        print("bot played 'paper'")
        print("YOU WON!")
    elif bot_play=="scissors":
        print("bot played 'scissors'")
        print("TIE!")                
else :
    print("invaild play ,you lost!")