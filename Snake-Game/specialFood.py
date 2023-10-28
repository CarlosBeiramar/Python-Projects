from turtle import Turtle
from food import Food

class SpecialFood(Food):

    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.color("gold1")
        self.shapesize(stretch_len=1.1, stretch_wid=1.1)