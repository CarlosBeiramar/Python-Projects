from turtle import Turtle
import random

COLORS = ["yellow", "red", "green", "OrangeRed", "DeepSkyBlue"]

class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()

        # normally the turtle is 20x20, with the next line of code it will be 10x10
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.color(random.choice(COLORS))
        self.refresh()
    
    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)
    
    def random_color(self):
        self.color(random.choice(COLORS))