import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
#screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player=Player()
car = CarManager()
score=Scoreboard()

screen.onkeypress(player.start_moving , "w")
screen.onkeyrelease(player.stop_moving , "w")

_time=0.1
game_is_on = True
while game_is_on:
    time.sleep(_time)
    screen.update()
    player.move()
    if player.ycor()>280:
        player.rest_pos()
        score.level+=1
        score.refresh()
        if _time >0.02:
            _time *= 0.8
    car.creat()
    car.move_car()
    for i in car.cars:
        if player.distance(i)<30:
            player.rest_pos()
            _time=0.1
            score.level=0
            score.refresh()
screen.exitonclick()