from turtle import Turtle, Screen
import random
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
X_COR_START = 20
Y_COR_START = 0

    
class Snake:
    
    def __init__(self):

        self.segments = []
        self.x_cor_start = X_COR_START
        self.y_cor_start = Y_COR_START
        self.create_snake()
        self.head = self.segments[0] 
        self.tail = self.segments[-1]
        
    def extend_snake(self):
        
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        tail_pos = self.tail.pos()
        new_segment.goto(tail_pos)
        self.segments.append(new_segment)
        
    def create_snake(self):
        
        for _ in range(3):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(self.x_cor_start, self.y_cor_start)
            self.segments.append(new_segment)
            self.x_cor_start -= 20

            
    def destroy_snake(self):
        
        for segment in self.segments:
            segment.ht()
        self.segments.clear()
        self.x_cor_start = X_COR_START
    
    def check_collision(self):
        
        body = self.segments[1:len(self.segments)]
        for i in body:
            if self.head.distance(i) < 15:
                return True
            
    def move(self):
        
        for i in range((len(self.segments)-1), 0, -1):
            pos = self.segments[i-1].pos()
            self.segments[i].goto(pos)
        self.head.fd(MOVE_DISTANCE)
        
    def move_up(self):
        
        if self.head.heading() != DOWN:
            self.head.seth(UP)
        
    def move_down(self):
        
        if self.head.heading() != UP:
            self.head.seth(DOWN)
        
    def move_left(self):
        
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
        
    def move_right(self):

        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
        
    