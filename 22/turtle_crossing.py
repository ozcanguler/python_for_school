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
screen.listen()    
screen.onkey(hero.go_up, "Up")
game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.go_left()