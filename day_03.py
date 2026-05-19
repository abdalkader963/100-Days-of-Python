#Fast and simple Treasure Island Game
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
direction=input("You're at a cross road. Where do you want to go?\n         Type 'left' or 'right'\n").lower()
if direction=="left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    time=input("Type 'wait' to wait for a boat. Type 'swim' to swim across\n").lower()
    if time=="wait":
        door=input("You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue. Which colour do you choose?").lower()
        if door=="red":
            print("you won!")
        else:
            print("game over")    
    else:
        print("game over")        
else:
    print("game_over")