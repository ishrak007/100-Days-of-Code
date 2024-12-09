from turtle import Turtle
import random

RT_UP = 35
RT_DOWN = -35
LT_UP = 145
LT_DOWN = 215
BALL_SPEED = 20

oklist = [55, 305, ]

class Ball(Turtle):
    
    def __init__(self):
        
        super().__init__()
        self.RT_UP = RT_UP
        self.RT_DOWN = RT_DOWN
        self.LT_UP = LT_UP
        self.LT_DOWN = LT_DOWN
        self.ball_speed = BALL_SPEED
        self.new_ball()
        
    def get_direction(self):
        
        head_right = random.randint(RT_DOWN, RT_UP)
        head_left = random.randint(LT_UP, LT_DOWN)
        random_heading = random.choice([head_left, head_right])
        self.seth(random_heading)
        # self.seth(150)
        
    def move(self):
        
        self.fd(self.ball_speed)
        
    def new_ball(self):
        
        self.clear()
        self.shape("circle")
        self.color("blue")
        self.pu()
        self.goto(0, 0)
        self.get_direction()
        
    def hit(self, paddle_body):
        
        for i in paddle_body:
            if i.distance(self) <= 20:
                self.ball_speed += 2
                return True
        