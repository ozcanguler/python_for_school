from turtle import Turtle,Screen
import random as r
don_ninja_turtle=Turtle()
don_ninja_turtle.shape("turtle")
don_ninja_turtle.color("purple","green")
screen = Screen()
screen.colormode(255)
def random_color():
    rgb_r=r.randint(0,255)
    rgb_g=r.randint(0,255)
    rgb_b=r.randint(0,255)
    random_color_input=(rgb_r,rgb_g,rgb_b)
    return random_color_input
def random_walk():
    i=0
    num=[0,90,180,270]
    colours=["dark orange","firebrick","magenta","navy","lime green","light gray","yellow"]
    don_ninja_turtle.pensize(10)
    while i<20:      
        don_ninja_turtle.forward(20)
        don_ninja_turtle.right(r.choice(num))
        don_ninja_turtle.pencolor(random_color())
        i+=1
def spirograph_walk(size):
    don_ninja_turtle.speed(0)
    for i in range(int(360/size)): 
        don_ninja_turtle.color(random_color())
        don_ninja_turtle.circle(100)
        don_ninja_turtle.setheading(don_ninja_turtle.heading()+size)

#random_walk()

spirograph_walk(10)
screen.exitonclick()

