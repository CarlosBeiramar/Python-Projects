from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x_cord, y_cord) -> None:
        super().__init__()
        self.shape('square')
        self.color("white")
        # all turtle start up with 20 x 20
        # we want 100 x 20
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_cord,y_cord)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
