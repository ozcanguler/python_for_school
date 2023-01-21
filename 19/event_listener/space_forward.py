from turtle import Turtle, Screen

raf_ninja_turtle=Turtle()
raf_ninja_turtle.shape("turtle")
raf_ninja_turtle.color("orange","green")
screen=Screen()

def move_forwards():
    raf_ninja_turtle.forward(10)
screen.listen()
screen.onkey(key="space",fun=move_forwards)
screen.exitonclick()

#Function as inputs
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def multi(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
def func(n1,n2,funcname):
    return funcname(n1,n2)
print(func(4,5,add))