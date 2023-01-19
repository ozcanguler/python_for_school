import colorgram
from turtle import Turtle,Screen
import random
import math
mic_ninja_turtle=Turtle()
mic_ninja_turtle.shape("turtle")
mic_ninja_turtle.color("red","green")
mic_ninja_turtle.speed(0)
mic_ninja_turtle.penup()
mic_ninja_turtle.setheading(225)
mic_ninja_turtle.forward(300)
mic_ninja_turtle.setheading(0)
screen = Screen()
colors=colorgram.extract("hirst.jpg",25)
first_color=colors[0]
print(first_color)
rgb = first_color.rgb
print(rgb[0],rgb[1],rgb[2])
rgbcolors=[]
for c in colors:
    r=c.rgb.r
    g=c.rgb.g
    b=c.rgb.b
    rgbcolorsnew=(r,g,b)
    rgbcolors.append(rgbcolorsnew)
#row_num=math.sqrt(len(rgbcolors))
#print(row_num)
for t in range(1,101):
    index=random.randint(0,24)
    dene='#%02x%02x%02x' % rgbcolors[index]
    mic_ninja_turtle.dot(20,dene)
    mic_ninja_turtle.forward(50)
    
    if(t%10==0):
        mic_ninja_turtle.setheading(90)
        mic_ninja_turtle.forward(50)
        mic_ninja_turtle.setheading(180)
        mic_ninja_turtle.forward(500)
        mic_ninja_turtle.setheading(0)
    #dene='#%02x%02x%02x' % (rgbcolors[t])
    #mic_ninja_turtle.fillcolor((dene));mic_ninja_turtle.begin_fill();mic_ninja_turtle.circle(10);mic_ninja_turtle.fd(50)
#mic_ninja_turtle.fd(50)
#mic_ninja_turtle.heading()
    #mic_ninja_turtle.end_fill()
screen.exitonclick()