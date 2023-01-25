from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard 
screen=Screen()#1
screen.setup(width=600,height=600)#1
screen.bgcolor("black")#1
screen.title("Snake Game")#1
screen.tracer(0)#1

snake=Snake()
food=Food() #5
scoreboard=Scoreboard() #7

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
    if snake.head.distance(food)<15:    #the snake's distance from the food #6
        print("nom nom nom")
        food.refresh()
        snake.extend()#9
        scoreboard.refresh_score()  #7
    if snake.head.xcor()>280 or snake.head.xcor() < -280 or snake.head.ycor()> 280 or snake.head.ycor()<-280:   #8
        is_game_start=False #8
        scoreboard.game_over()  #8
    for segment in snake.segments[1:]:#10
        if snake.head.distance(segment)<10:
            is_game_start=False
            scoreboard.game_over()
screen.exitonclick()#1