from turtle import Screen
import time
from snake_class import *
from food_class import *
from score_class import Scoreboard

screen = Screen()
screen.screensize(canvwidth=550, canvheight=550)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)

game_end = False
while not game_end:

    screen.update()
    time.sleep(0.1)
    snake.move()
    food.keep_moving()
    head_x = snake.head.xcor()
    head_y = snake.head.ycor()
    
    if snake.head.distance(food) < 20:
        food.appear()
        snake.extend_snake()
        score.update_scoreboard()
        
    collision = snake.check_collision()     
    if collision or head_x >= 285 or head_x <= -305 or head_y >= 305 or head_y <= -285:
        score.reset_game()
        snake.destroy_snake()
        snake.create_snake()
        snake.head = snake.segments[0]
        snake.tail = snake.segments[-1]
        score.new_scoreboard()
        # game_end = True      

screen.exitonclick()
