from turtle import Turtle, Screen
import random
screen=Screen()
screen.setup(width=500,height=600)
point1 = (230, -200)
point2 = (230, 200)
finish_line=Turtle()
finish_line.penup()
finish_line.goto(point1)
finish_line.pendown()
finish_line.goto(point2)
finish_line.hideturtle()

answer = screen.textinput("Welcome to Turtle Race!","red/purple/yellow/orange/black/blue/green/gray Enter a color:")
colors=["red","purple","yellow","orange","black","blue","green","gray"]
y_coord=[-100,-70,-40,-10,50,80,110]
all_turtles=[]
if answer in colors:
    colors.remove(answer)
else:
    answer="black"
    colors.remove("black")
for i in colors:
    print(i)
my_turtle=Turtle(shape="turtle")
my_turtle.penup()
my_turtle.goto(x=-230,y=20)
my_turtle.color(f"{answer}")
all_turtles.append(my_turtle)



for turtles in range(0,7):
    race_turtle=Turtle(shape="turtle")
    race_turtle.penup()
    race_turtle.goto(x=-230,y=y_coord[turtles])
    race_turtle.color(colors[turtles])
    all_turtles.append(race_turtle)
if answer:
    is_race_start=True

while is_race_start:
    for t in all_turtles:
        if t.xcor()>210:
            is_race_start=False
            winning_turtle=t.pencolor()
            if winning_turtle==answer:
                print(f"You've won{winning_turtle}")
            else:
                print(f"You've lost. The {winning_turtle} turtle is won")             

        rand_forward=random.randint(0,10)
        t.forward(rand_forward)
screen.exitonclick()