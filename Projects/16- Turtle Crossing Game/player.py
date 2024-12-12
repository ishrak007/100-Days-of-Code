from turtle import Turtle
START_POS = (0, -280)
CROSSER_SPEED = 10
FINISH_LINE_Y = 280

class Crosser(Turtle):
    
    def __init__(self):
        
        super().__init__()
        self.start_pos = START_POS
        self.crosser_speed = CROSSER_SPEED
        self.create_crosser()
        
    def create_crosser(self):
        
        self.clear()
        self.shape("turtle")
        self.pu()
        self.color("black")
        self.seth(90)
        self.goto(self.start_pos)
        
    def move_up(self):
        
        self.fd(self.crosser_speed)
        
    def move_down(self):
        
        self.bk(self.crosser_speed)
        
