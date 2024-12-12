from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()
        self.hideturtle()
        self.color("white")
        self.pu()
        self.score_a = 0
        self.score_b = 0
        self.create_scoreboard()
        
    def create_scoreboard(self):
        
        self.clear()
        self.goto(-200, 260)
        self.write(
            arg=f"{self.score_a}", move = False, align="center", 
            font=("Courier New", 20, "bold")
            )
        self.goto(200, 260)
        self.write(
            arg=f"{self.score_b}", move = False, align="center", 
            font=("Courier New", 20, "bold")
            )
        
    def update_score_a(self):
        
        self.score_a += 1
        self.create_scoreboard()
        
    def update_score_b(self):
        
        self.score_b += 1
        self.create_scoreboard()

