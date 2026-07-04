COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 8
MOVE_INCREMENT = 10
from turtle import Turtle
import random
class CarManager():
    def __init__(self):
        self.cars=[]
        self.cars.append(self.car())
#Creat the car        
    def creat(self):
        i=random.randint(1,6)
        if i == 1:
            if len(self.cars) == 0 or self.cars[-1].xcor()<240:
                self.street_car=self.car()
                self.cars.append(self.street_car)
#make it move
    def move_car(self):
        for car in self.cars:
            x=car.xcor()
            y=car.ycor()
            car.goto(x-STARTING_MOVE_DISTANCE ,y)
            if car.xcor() < -320:
                car.hideturtle()
                self.cars.remove(car)            
#The car build
    def car(self):
        turtle =Turtle()
        turtle.penup()
        turtle.shape("square")
        turtle.color(random.choice(COLORS))
        turtle.setheading(180)
        turtle.turtlesize(stretch_wid=1 , stretch_len=2)
        y=random.randint(-250,250)
        turtle.goto(280,y)
        return turtle

