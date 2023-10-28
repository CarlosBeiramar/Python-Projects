from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")

class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(0,270)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
    
    def increase_score(self, boolean):
        if boolean:
            self.score += 2
            self.clear()
            self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        else:
            self.score += 1
            self.clear()
            self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGNMENT,font = FONT)