STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.is_moving=False

    def start_moving(self):
        self.is_moving=True        

    def stop_moving(self):
        self.is_moving=False

    def move(self):
        if self.is_moving :
            self.fd(MOVE_DISTANCE)

    def rest_pos(self):
        self.goto(STARTING_POSITION)
