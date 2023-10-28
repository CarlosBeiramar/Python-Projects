from turtle import Turtle

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self) -> None:

        self.squares = []
        self.create_snake()
        self.head = self.squares[0]
        self.move_speed = 0.1
    
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_square(position)
    
    def add_square(self, position):
        square = Turtle(shape='square')
        square.color('white')
        square.penup()
        square.goto(position)
        self.squares.append(square)
        
    def extend(self):
        #add square to the snake
        self.add_square(self.squares[-1].position())

    def move(self):
        for square_num in range(len(self.squares) - 1, 0,-1):
            # This will iterate from the last element of the list
            # to the head of the list
            # In the first iteration:
                # the last element go to the position of the last-1 element
            new_x = self.squares[square_num-1].xcor()
            new_y = self.squares[square_num-1].ycor()
            self.squares[square_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def across_wall_right(self):
        self.head.goto(-280, self.head.ycor())
    
    def across_wall_left(self):
        self.head.goto(280, self.head.ycor())
    
    def across_roof(self):
        self.head.goto(self.head.xcor(), -280)
    
    def across_floor(self):
        self.head.goto(self.head.xcor(), 280)

    def change_snake_color(self, color):
        for square in self.squares:
            square.color(color)

    def snake_speed_up(self):
        for square in self.squares:
            square.speed(10)

    def increase_speed(self):
        self.move_speed *= 0.9