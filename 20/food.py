from turtle import Turtle
import random
class Food(Turtle): #5
    def __init__(self): #5
        super().__init__()  #5
        self.shape("circle")    #5
        self.penup()    #5
        self.shapesize(stretch_len=0.5,stretch_wid=0.5) #5
        self.color("white")  #5
        self.speed(0)   #5
        rand_x=random.randint(-280,280) #5
        rand_y=random.randint(-280,280) #5
        self.goto(rand_x,rand_y)    #5
