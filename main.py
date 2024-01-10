import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle CrossyRoad")
screen.tracer(0)

player = Player()

screen.listen()
screen.onkeypress(player.move_up, "Up")

car_manager = CarManager()

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    if player.ycor() > FINISH_LINE_Y:
        player.reset_position()
        scoreboard.increase_level()
        car_manager.speed_up()

    # Detect collision with car
    for car in car_manager.cars:
        if car.distance(player) < 15:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
