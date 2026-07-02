#Creat the plear's paddle
from turtle import Turtle
class Paddle(Turtle):
    def __init__(self , xcore , ycore):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.turtlesize(  stretch_wid= 5,stretch_len= 1 , outline= 5)
        self.penup()
        self.setposition(xcore , ycore)

    def up(self):
        y=self.ycor() +30
        self.goto(self.xcor(), y)
    def down(self):
        y=self.ycor() -30
        self.goto(self.xcor(), y) 