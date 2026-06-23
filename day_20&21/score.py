from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.goto(x=0 , y=260)
        self.write(f"Score : {self.score}",False , align= "center", font=("Courier", 24, "normal"))
    def inc_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score : {self.score}",False , align= "center", font=("Courier", 24, "normal"))

        
