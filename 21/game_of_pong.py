from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball() 
scoreboard=Scoreboard()

screen.listen()    
screen.onkey(r_paddle.pong_up, "Up")
screen.onkey(r_paddle.pong_down, "Down")
screen.onkey(l_paddle.pong_up, "w")
screen.onkey(l_paddle.pong_down, "s")
game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move() 
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    if ball.distance(r_paddle)<55 and ball.xcor()>320 or ball.distance(l_paddle)<55 and ball.xcor()<-320:
        ball.bounce_x()
    if ball.xcor()>350:
        ball.reset_ball_p()
        scoreboard.l_point()
    if ball.xcor()<-350:
        ball.reset_ball_p()
        scoreboard.r_point()
screen.exitonclick()