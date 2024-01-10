from turtle import Turtle

FONT = ("Courier", 24, "bold")
ALIGNMENT = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-275, 250)
        self.write(arg=f"Level: {self.level}", align=ALIGNMENT, font=FONT)
    
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)
