import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
# setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.tracer(0)
# create player turtle and car turtle

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()




screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.car_move()

    for car in car_manager.all_cars:

        # detect collision with car
        if player.distance(car) < 25:
            scoreboard.game_over()
            game_is_on = False

            # increase score
        if player.is_at_finish_line():
            player.refresh()
            car_manager.level_up()





screen.exitonclick()
