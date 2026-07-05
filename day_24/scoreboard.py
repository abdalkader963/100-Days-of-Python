from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open(r"C:\Users\E-store\Desktop\py_journey\100-Days-of-Python\day_24\save_game.txt" , mode= "r") as save:
            self.high_score=int(save.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score >self.high_score:
            self.high_score=self.score
            with open(r"C:\Users\E-store\Desktop\py_journey\100-Days-of-Python\day_24\save_game.txt" , mode="w") as save:
                save.write(str(self.score)) 
        self.score=0
        self.update_scoreboard()    

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
