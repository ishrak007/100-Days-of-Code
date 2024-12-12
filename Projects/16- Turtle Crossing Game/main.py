import time
from turtle import Screen
from player import *
from cars import *
from score import *

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

crosser = Crosser()
score = Scoreboard()
car_manager = Car_Manager()

screen.listen()
screen.onkey(crosser.move_up, "Up")
screen.onkey(crosser.move_down, "Down")

game_end = False
counter = 1
while not game_end:
    
    time.sleep(0.1)
    screen.update()
    
    # Generate a car instance at a random position every 0.3 seconds
    if counter % 5 == 0:
        car = Car()
        car_manager.add_car(car)
    
    # Move all the car instances
    car_manager.move_cars()
    
    # Check collision
    hit = car_manager.check_collision(crosser) 
    if hit:
        score.end_game()
        game_end = True
    
    # Get rid of displayed cars from memory
    car_manager.remove_cars()
    
    pos_y = crosser.ycor()
    pos_x = crosser.xcor()
    
    # Check if racer reached finish line
    if pos_y >= 280:
        
        car_manager.raise_speed()
        score.update_scoreboard()
        crosser.create_crosser()
        counter = 1
        
    # Don't let racer go underneath the screen 
    if pos_y <= crosser.start_pos[1]:
        
        crosser.goto(crosser.start_pos)
        
    counter += 1

screen.exitonclick()