from turtle import Turtle, Screen
from paddle import *
from ball import *
from score import *
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('The Pong Game')
screen.tracer(0)


paddle_left = Paddle(X_LEFT, Y_LEFT)
paddle_right = Paddle(X_RIGHT, Y_RIGHT)
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")
screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")


# if paddle_left.top.distance(X_LEFT, 287) <= 50:
#     paddle_left.stop_moving()


game_end = False

while not game_end:
    
    screen.update()
    time.sleep(0.1)
    
    ball.move()
    
    pos_x = ball.xcor()
    pos_y = ball.ycor()
    direction = ball.heading()
    hit_left = ball.hit(paddle_left.paddle_body)
    hit_right = ball.hit(paddle_right.paddle_body)
    
    # Collision with wall
    if pos_y > 280:
        ball.seth(-direction)
    elif pos_y < -280:
        ball.seth(-direction)
    # Collision with paddles
    elif hit_left or hit_right:
        angle_of_incidence = 90 - direction
        new_direction = 90 + angle_of_incidence
        ball.seth(new_direction)
        ball.fd(10)
    # Score tracking and refreshing ball
    elif pos_x > 420:
        score.update_score_a()
        ball.new_ball()
    elif pos_x < -440:
        score.update_score_b()
        ball.new_ball()

screen.exitonclick()