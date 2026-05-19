# This is a simple number guessing game where the user has to guess a random number between 1 and 30. The user has 7 tries to guess the number correctly. After each guess, the program will provide feedback on whether the guess is too low, too high, or correct. If the user runs out of tries, they lose the game.
import random
number_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
random_number=random.choice(number_list)
print(random_number) 
goal=False
trys=7
while not goal:
    user_guess=int(input("guess the number between 1 and 30\n"))
    if user_guess==random_number:
        print("you win!")
        goal=True
    elif user_guess<random_number:
        print("too low") 
        trys-=1
        user_guess=int(input("guess the number between 1 and 30\n"))
    elif user_guess>random_number:
        print("too high")
        trys-=1
        user_guess=int(input("guess the number between 1 and 30\n"))
    else:
        print("invalid input")
        user_guess=int(input("guess the number between 1 and 30\n"))   
    if trys==0:
        goal=True
        print("you lose!")