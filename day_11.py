#simple blackjack game
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def calculate_score(player):
    player_score = sum(player)
    if 11 in player and player_score > 21:
        player.remove(11)
        player.append(1)
        player_score = sum(player)
    return player_score
def user_gameplay(user, bot, bot_score):
    user_score = calculate_score(user)
    while user_score < 21:
        choice = input("Type 'y' to get another card, type 'n' to pass: ")
        if choice == "y":
            ran = random.sample(cards, 1)
            user.append(ran[0])
            user_score = calculate_score(user)
            print(f"Your cards: {user}, current score: {user_score}")
        elif choice == "n":
            break
    while bot_score < 17 and user_score <= 21:
        bot.append(random.sample(cards, 1)[0])
        bot_score = calculate_score(bot)
    print(f"\nYour final hand: {user}, final score: {user_score}")
    print(f"Computer's final hand: {bot}, final score: {bot_score}")
    if user_score > 21:
        print("You went over. You lost!")
    elif bot_score > 21:
        print("Opponent went over. You won!")
    elif user_score > bot_score:
        print("You won!")
    elif user_score == bot_score:
        print("Tie!")
    else:
        print("You lost!")
goal=False
game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while not goal:
    if game == "y":
        user = random.sample(cards, 2)
        bot= random.sample(cards, 2)
        user_score = calculate_score(user)
        bot_score = calculate_score(bot)
        print(f"Your cards: {user}, current score: {user_score}")
        print(f"Computer's first card: {bot[0]}")
        user_gameplay(user, bot, bot_score)
        goal=True
    again=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if again=="y":
        clear_screen()
        goal=False
    else:  
        clear_screen()  