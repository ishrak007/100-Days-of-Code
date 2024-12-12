from turtle import Turtle
FONT = ("Courier", 18, "bold")

class Scoreboard(Turtle):
    
    def __init__(self):
        
        super().__init__()
        self.color("Black")
        self.hideturtle()
        self.pu()
        self.score = 0
        self.font = FONT
        self.goto(-280, 260)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        
        self.score += 1
        self.clear()
        self.write(arg = f"Level: {self.score}", move = False, 
                   align="left", font = self.font
                   )
        
    def end_game(self):
        
        self.goto(0, 0)
        self.write(arg = f"Game Over", move = False, 
                   align="center", font = self.font
                   )
