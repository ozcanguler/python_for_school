from turtle import Screen
import time
from snake import Snake
from food import Food 
screen=Screen()#1
screen.setup(width=600,height=600)#1
screen.bgcolor("black")#1
screen.title("Snake Game")#1
screen.tracer(0)#1

snake=Snake()
food=Food() #5

screen.listen()
screen.onkey(snake.up, "Up")    #4
screen.onkey(snake.down, "Down")    #4
screen.onkey(snake.left, "Left")    #4
screen.onkey(snake.right, "Right")  #4

is_game_start=True#2
while is_game_start:#2
    screen.update()#2
    time.sleep(0.1)#2
    snake.move() 
screen.exitonclick()#1