from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from score import Score
score=Score()
screen=Screen()
screen.setup(width= 800 , height= 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
ball = Ball(score)
r_pad=Paddle(350 , 0)
l_pad=Paddle(-350 , 0)
screen.listen()
screen.onkey(r_pad.up,"Up")
screen.onkey(r_pad.down, "Down")
screen.onkey(l_pad.up,"w")
screen.onkey(l_pad.down, "s")
game_on = True

while game_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    ball.wall_Collision()
    ball.paddle_Collision(r_pad)
    ball.paddle_Collision(l_pad)
    if ball.goal():
        score.inc_score()
        
screen.exitonclick()