from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        x_pos, y_pos = 0, 275
        self.goto(x_pos, y_pos)
        self.playerscore = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(F"Score: {self.playerscore} / 50", align=ALIGNMENT, font=FONT)
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def victory(self):
        self.goto(0,0)
        self.color("red")
        self.write("CONGRATULATIONS, YOU WON!", align=ALIGNMENT, font=FONT)