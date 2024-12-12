import random
from turtle import Turtle, Screen
X_LEFT = -387
X_RIGHT = 380
Y_LEFT = random.randint(-219, 287)
Y_RIGHT = random.randint(-219, 287)
SPEED = 25
PADDLE_SIZE = 4

class Paddle():
    
    def __init__(self, X_POS, Y_POS):
        
        # super().__init__()
        self.x_pos = X_POS
        self.y_pos = Y_POS
        self.paddle_body = []
        self.create_paddle()
        self.top = self.paddle_body[0]
        self.bottom = self.paddle_body[-1]
        
    def create_paddle(self):
        
        for _ in range(PADDLE_SIZE):
            new_square = Turtle("square")
            new_square.color("white")
            new_square.pu()
            new_square.speed(0)
            new_square.goto(self.x_pos, self.y_pos)
            self.paddle_body.append(new_square)
            self.y_pos -= 20
            
    def move_up(self):
        
        for i in reversed(self.paddle_body):
            i.seth(90)
            i.fd(SPEED)
            
    def move_down(self):
        
        for i in self.paddle_body:
            i.seth(270)
            i.fd(SPEED)
            
        

        
