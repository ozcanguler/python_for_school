from turtle import Screen,Turtle
from paddle import Paddle
screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))



screen.listen()    
screen.onkey(r_paddle.pong_up, "Up")
screen.onkey(r_paddle.pong_down, "Down")
screen.onkey(l_paddle.pong_up, "w")
screen.onkey(l_paddle.pong_down, "s")
game_is_on=True
while game_is_on:
    screen.update()#2
screen.exitonclick()