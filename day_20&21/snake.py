from  turtle import Turtle
STARTING=[(0,0),(-20,0),(-40,0)]
MOVE_DIS=20
class Snake:
    def __init__(self):
          self.segments=[]
          self.creat()
    def creat(self):
        for pos in STARTING:
            new_seg=Turtle(shape="square")
            new_seg.penup() 
            new_seg.color("white")
            new_seg.goto(pos)
            self.segments.append(new_seg)
            self.head=self.segments[0]

    def move(self):
            for seg in range(len(self.segments)-1 , 0 ,-1):
                x=self.segments[seg -1].xcor()
                y=self.segments[seg -1].ycor()
                self.segments[seg].goto(x , y)
            self.head.fd(MOVE_DIS)
    def up(self):
            if self.head.heading()!=270:
                self.head.setheading(90)
    def down(self):
            if self.head.heading()!=90:
                self.head.setheading(270)            
    def left(self):
            if self.head.heading()!=0:    
                self.head.setheading(180)                 
    def right(self):
            if self.head.heading()!=180:
                self.head.setheading(0)             