import time
from turtle import Screen
from hero import Hero
from cars import Cars
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

hero=Hero()
cars=Cars()
scoreboard=Scoreboard()
screen.listen()    
screen.onkey(hero.go_up, "Up")
game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.go_left()

    for car in cars.all_cars:
        if car.distance(hero)<20:
            game_is_on=False
            scoreboard.game_over()
    if hero.finish_line():
        hero.go_to_start_position()
        cars.level_up()
        scoreboard.increase_level()
screen.exitonclick()