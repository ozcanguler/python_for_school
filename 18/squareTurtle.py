from turtle import Turtle,Screen
import random as r
leo_ninja_turtle=Turtle()
leo_ninja_turtle.shape("turtle")
leo_ninja_turtle.color("blue","green")

def square_turtle():
    i=0
    while i<4:
        leo_ninja_turtle.forward(100)
        leo_ninja_turtle.right(90)
        i+=1
def draw_and_nondraw_square_turtle():
    leo_ninja_turtle.penup()
    leo_ninja_turtle.goto(-50, 200)
    leo_ninja_turtle.pendown()
    i=0
    while i<4:
        leo_ninja_turtle.pendown() 
        leo_ninja_turtle.forward(20)
        leo_ninja_turtle.right(90)
        leo_ninja_turtle.penup() 
        leo_ninja_turtle.forward(20)      
        i+=1
def unlimitedgon_turtle():
    colours=["dark orange","firebrick","magenta","navy","lime green","light gray","yellow"]
    leo_ninja_turtle.penup()
    leo_ninja_turtle.goto(-50, -100)
    leo_ninja_turtle.pendown()
    i=2
    while i<8:
        j=0
        i+=1
        leo_ninja_turtle.pencolor(r.choice(colours))
        while j<i:
            leo_ninja_turtle.forward(100)
            leo_ninja_turtle.right(360/i)
            j+=1
leo_ninja_turtle.penup()
leo_ninja_turtle.goto(-50, 100)
leo_ninja_turtle.pendown()
square_turtle()
draw_and_nondraw_square_turtle()
unlimitedgon_turtle()
screen = Screen()
screen.exitonclick()