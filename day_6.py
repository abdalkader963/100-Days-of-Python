#maze slover robot (works in reeborgs world)
# take 1- my own mind with no outer help works 100% fine
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while at_goal() != True :
    def jump():
        if right_is_clear()!=True:
            turn_left()
            if  front_is_clear() ==True:
                move()
            elif right_is_clear() ==True:                
                turn_left()
                move()
            elif  right_is_clear() !=True and front_is_clear() != True:
                turn_left()
                move()
            else:
                move()
        elif right_is_clear() == True:
            turn_right()
            move()
            turn_right()
            if front_is_clear() == True:
                move()
            else:
                turn_left()
        else:
            move()
    if front_is_clear() != True:
        jump()
    elif right_is_clear() == True:
        turn_right()
        move()
    elif front_is_clear() == True:
        move()    
    else:
        move()
# take 2- just orgnized my code using AI 
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def solve():
    if right_is_clear():   
        turn_right()
        move()
    elif front_is_clear(): 
        move()
    else:                    
        turn_left()
while not at_goal():
    solve()