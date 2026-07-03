from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1, outline=5)
        self.penup()
        self.setposition(x_pos, y_pos)

    def up(self):
        if self.ycor() < 240:
            y = self.ycor() + 30
            self.goto(self.xcor(), y)

    def down(self):
        if self.ycor() > -240:
            y = self.ycor() - 30
            self.goto(self.xcor(), y)