from turtle import Turtle, Screen
import random

class Food(Turtle):
    
    def __init__(self):
        
        super().__init__()
        self.shape("circle")
        self.pu()
        self.color('red')
        self.shapesize(0.5, 0.5)
        self.appear()

    def appear(self):
        
        self.speed(0)
        x_pos = random.randint(-255, 255)
        y_pos = random.randint(-255, 255)
        self.goto(x_pos, y_pos)
        
    def keep_moving(self):
        
        self.speed(8)
        self.fd(5)
        self.rt(90)
        