from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

food = Food()
score=Score()
score.show_score()
scr=Screen()
scr.setup(width=600 , height= 600)
scr.bgcolor("black")
scr.title("Snake game")
scr.tracer(0)
snake=Snake()
game_on=True

scr.listen() 
scr.onkey(snake.up ,"Up")
scr.onkey(snake.down ,"Down")
scr.onkey(snake.left ,"Left")
scr.onkey(snake.right ,"Right")

while game_on:
    scr.update()    
    time.sleep(0.1)
    snake.move()
    #detect collision with food.
    if snake.head.distance(food) <17:
        food.refresh()
        score.inc_score()
        snake.extend()
    #detect collision with wall.        
    if snake.wall_Collision() == False:
        score.over()
        game_on=False
    #detect collision with it self.        
    if snake.check_snake() == False:
        score.over()
        game_on=False

scr.exitonclick()