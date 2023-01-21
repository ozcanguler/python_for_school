from turtle import Turtle, Screen

ant=Turtle()
screen=Screen()
def move_forwards():
    ant.forward(10)
def move_backforwards():
    ant.backward(10)
def move_counterclockwise():
    ant.left(10)
def move_clockwise():
    ant.right(10)
def ant_clear():
    ant.clear()
    ant.penup()
    ant.home()
    ant.pendown()   
screen.listen()
screen.onkey(key="w",fun=move_forwards)
screen.onkey(key="s",fun=move_backforwards)
screen.onkey(key="a",fun=move_counterclockwise)
screen.onkey(key="d",fun=move_clockwise)
screen.onkey(key="c",fun=ant_clear)
screen.exitonclick()