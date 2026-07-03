import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

score = Score()
ball = Ball()
r_pad = Paddle(350, 0)
l_pad = Paddle(-350, 0)

screen.listen()
screen.onkey(r_pad.up, "Up")
screen.onkey(r_pad.down, "Down")
screen.onkey(l_pad.up, "w")
screen.onkey(l_pad.down, "s")

game_on = True
time_sleep = 0.1

while game_on:
    time.sleep(time_sleep)
    screen.update()
    
    ball.move()
    ball.wall_collision()
    
    if ball.paddle_collision(r_pad) or ball.paddle_collision(l_pad):
        if time_sleep > 0.03:
            time_sleep *= 0.9
            
    scorer = ball.check_goal()
    if scorer == "left":
        score.l_point()
        time_sleep = 0.1
    elif scorer == "right":
        score.r_point()
        time_sleep = 0.1

screen.exitonclick()