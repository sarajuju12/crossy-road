from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        
    def create_car(self):
        chance = random.randint(1, 7)
        if chance == 7:
            car = Turtle("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(COLORS))
            car.penup()
            car.goto(300, random.randint(-250, 250))
            self.cars.append(car)
         
    def move(self):
        for car in self.cars:
            car.backward(self.speed)
    
    def speed_up(self):
        self.speed += MOVE_INCREMENT
