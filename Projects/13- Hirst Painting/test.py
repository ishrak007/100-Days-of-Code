from turtle import Turtle, Screen
import turtle
import random
from color_extraction import new_colors_list

def get_color(color_list):
    return random.choice(color_list)

a = [(0, 1, 2), (1, 5, 3), (2, 6, 9)]
print(get_color(new_colors_list))