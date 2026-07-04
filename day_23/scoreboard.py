FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-200 , y=250)
        self.level=0
        self.write(f"LEVEL : {self.level}",False , align= "center", font=("Courier", 24, "normal"))
        
    def refresh(self):
        self.clear()
        self.write(f"LEVEL : {self.level}",False , align= "center", font=("Courier", 24, "normal"))