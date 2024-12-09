from turtle import Turtle, Screen
import turtle
import random
from color_extraction import new_colors_list

def draw_dots(x_init, y_init, color_list):
    for _ in range(11):
        y_init += 55
        for _ in range(10):
            turty.dot(20, get_color(color_list))
            turty.fd(50)
        turty.dot(20, get_color(color_list))
        turty.teleport((x_init), (y_init))
        
def get_color(color_list):
    return random.choice(color_list)

# Main

turtle.colormode(255)
turty = Turtle()
turty.shape("classic")
turty.pensize(2)
turty.speed(10)
turty.pu()
turty.hideturtle()
x_init = -250
global y_init
y_init = -300
turty.teleport(x_init, y_init)
draw_dots(x_init, y_init, new_colors_list)

screen = Screen()
screen.exitonclick()