from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
CAR_SPEED_START = 20
SPEED_INCREMENT = 5

class Car(Turtle):
    
    def __init__(self):
        
        super().__init__()
        self.colors = COLORS
        self.start_x = random.randint(320, 350)
        self.start_y = random.randint(-245, 245)
        self.shape("square")
        self.color(random.choice(self.colors))
        self.speed(0)
        self.shapesize(1, 2)
        self.seth(180)
        self.pu()
        self.generate_car()
        
    def generate_car(self):
        
        x_cor = self.start_x
        y_cor = self.start_y
        self.goto(x_cor, y_cor)
    
class Car_Manager():
    
    def __init__(self):
        
        self.car_speed = CAR_SPEED_START
        self.speed_increment = SPEED_INCREMENT
        self.end_x = -340
        self.cars_list = []
    
    def add_car(self, car_instance):
        
        """Bring a new car to the screen's right edge"""
        self.cars_list.append(car_instance)
        
    def raise_speed(self):
        
        """Raise the speed of the cars when called"""
        self.car_speed += self.speed_increment
    
    def move_cars(self):
        
        """Move cars by the speed specified"""
        for i in self.cars_list:
            i.fd(self.car_speed)
            
    def remove_cars(self):
        """remove already displayed cars"""
        for i in self.cars_list[:]:
            pos_x = i.xcor()
            if pos_x <= self.end_x:
                i.ht()
                self.cars_list.remove(i)    
                
    def check_collision(self, crosser):
        
        """Detects collision with crosser"""
        for i in self.cars_list:
            if crosser.distance(i) < 20:
                return True