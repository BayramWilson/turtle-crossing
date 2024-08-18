import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
# setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
# create player turtle and car turtle
smoky = Player()

scoreboard = Scoreboard()


screen.listen()
car = CarManager()
car2 = CarManager()
car3 = CarManager()
car4 = CarManager()
car5 = CarManager()
car6 = CarManager()
car7 = CarManager()

game_is_on = True
while game_is_on:
    car = CarManager()
    car2.car_move()
    car3.car_move()
    car4.car_move()
    car5.car_move()
    car6.car_move()
    car7.car_move()
    screen.onkey(smoky.move, "Up")
    time.sleep(0.1)
    screen.update()
    # increase score
    if smoky.ycor() == 280:
        smoky.refresh()
        scoreboard.increase_score()
    # detect collision with car
    if smoky.distance(car) < 20 or smoky.distance(car2) < 20 or smoky.distance(car3) < 20 or smoky.distance(car4) < 20 or smoky.distance(car5) < 20 or smoky.distance(car6) < 20 or smoky.distance(car7) < 20:
        scoreboard.game_over()
        smoky.refresh()


screen.tracer(0)
screen.exitonclick()
