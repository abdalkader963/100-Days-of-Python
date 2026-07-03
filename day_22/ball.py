from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.xmove = 10
        self.ymove = 10

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def wall_collision(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.ymove *= -1

    def paddle_collision(self, pad):
        # Checks distance and ensures the ball is moving toward the paddle to prevent sticking
        if self.distance(pad) < 50:
            if self.xcor() > 320 and self.xmove > 0:
                self.xmove *= -1
                return True
            elif self.xcor() < -320 and self.xmove < 0:
                self.xmove *= -1
                return True
        return False

    def check_goal(self):
        if self.xcor() > 380:
            self.reset_ball()
            return "left"
        elif self.xcor() < -380:
            self.reset_ball()
            return "right"
        return None

    def reset_ball(self):
        self.goto(0, 0)
        self.xmove *= -1