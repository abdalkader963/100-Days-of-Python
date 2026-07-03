from turtle import Turtle
class Ball(Turtle):
    
    def __init__(self, score):
        super().__init__()
        self.score = score
        self.shape("circle")
        self.penup()
        self.color("white")
        self.xmove = 10
        self.ymove =10
        self.goals=0

    def move(self):
        self.new_x=self.xcor() +self.xmove
        self.new_y=self.ycor() +self.ymove
        self.goto(self.new_x , self.new_y)

    def wall_Collision(self):
        if self.ycor() >280 or self.ycor()<-280:
            self.ymove *= -1
        else:
            pass    

    def paddle_Collision(self , r_pad):
            if( self.xcor() >320 or self.xcor()<-320 )and self.distance(r_pad)<50:
                self.xmove *= -1
            else:
                pass           

    def goal(self):
        if self.xcor()>380:
            self.goto(0,0)
            self.xmove*= -1
            self.score.l_score +=1
            return True
        elif self.xcor()<-380:
            self.goto(0,0)
            self.xmove*= -1  
            self.score.r_score +=1
            return True
        return False