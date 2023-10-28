from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from specialFood import SpecialFood
import time

# define my window
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
# Turn turtle animation on/off and set delay for update drawings
screen.tracer(0)

snake = Snake()
food = Food()
specialFood = None
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


# Update screen after create squares
screen.update()
game_is_on = True
flag_specialFood = True


while game_is_on:
    screen.update()
    time.sleep(snake.move_speed)
    snake.move()
    snake.snake_speed_up()


    if scoreboard.score % 5 == 0 and flag_specialFood:
        specialFood = SpecialFood()
        flag_specialFood = False

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()  
        snake.extend()
        snake.change_snake_color(food.color()[1])
        food.random_color()
        scoreboard.increase_score(False)

    if specialFood:
        if snake.head.distance(specialFood) < 15:
            snake.extend()
            snake.extend()
            snake.change_snake_color(snake.head.color()[1])
            scoreboard.increase_score(True)
            specialFood.goto(350,0)
            flag_specialFood = True
            snake.increase_speed()

    if snake.head.xcor() > 280:
        snake.across_wall_right()

    elif snake.head.xcor() < -280:
        snake.across_wall_left()

    elif snake.head.ycor() > 280:
        snake.across_roof()
    
    elif snake.head.ycor() < -280:
        snake.across_floor()
    
    #Detect collision with tail.
    for square in snake.squares[1:]:
        if snake.head.distance(square) < 10:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()