from turtle import Turtle
SCORE_START = 0

class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()
        self.highest_score = 0
        self.goto(0, 270)
        self.color("white")
        self.pu()
        self.hideturtle()
        self.score = SCORE_START
        # self.create_scoreboard()
        self.new_scoreboard()
        
    def create_scoreboard(self):
        self.clear()
        self.write(
            arg=f"Score: {self.score} | Highest Score: {self.highest_score}", 
            move=False, align="center", font=("Comic Sans MS", 15, "bold")
        )
        
    def update_scoreboard(self):
        self.score += 1
        self.clear()
        self.write(
            arg=f"Score: {self.score} | Highest Score: {self.highest_score}", 
            move=False, align="center", font=("Comic Sans MS", 15, "bold")
        )

    def reset_game(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
        self.score = 0
        self.clear()
        with open(r"D:\CODED_LIFE\###Udemy-100 Days of Pyt\Projects\14- Snake Game\highest_score.txt", mode="w") as file:
            file.write(f"{self.highest_score}")
            
    def new_scoreboard(self):
        with open(r"D:\CODED_LIFE\###Udemy-100 Days of Pyt\Projects\14- Snake Game\highest_score.txt", mode="r") as file:
            info = file.read()
        self.highest_score = int(info)
        self.write(
            arg=f"Score: {self.score} | Highest Score: {self.highest_score}", 
            move=False, align="center", font=("Comic Sans MS", 15, "bold")
        )

    # def end_game(self):
    #     self.home()
    #     self.write(
    #         arg=f"GAME OVER", move=False, align="center", font=("Comic Sans MS", 15, "bold")
    #     )


