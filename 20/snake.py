from turtle import Turtle
import random
positions=[(0,0),(-20,0),(-40,0)]#1
move=20
up=90 #5
down=270 #5
left=180 #5
right=0 #5
colors=("blue","red","green")
class Snake():
    def __init__(self):
        super().__init__()
        self.segments=[]
        self.createSnake()
        self.head=self.segments[0]  #4
    def createSnake(self):
        for i in positions:#1
            #my_snake=Turtle(shape="square")#1
            #my_snake.penup()#2
            #my_snake.goto(positions[i])#1
            #my_snake.color(colors[i])#1
            #self.segments.append(my_snake)#2
            self.add_tail(i)
    def move(self):
        for s in range(len(self.segments)-1,0,-1):#3
            new_x=self.segments[s-1].xcor()#3
            new_y=self.segments[s-1].ycor()#3
            self.segments[s].goto(new_x,new_y)#3
        self.head.forward(move) #3
        #self.segments[0].left(30)   #3
    def up(self):#4
        if self.head.heading()!=down:
            self.head.setheading(up)
    def down(self):#4
        if self.head.heading()!=up:
            self.head.setheading(down)
    def left(self):#4
        if self.head.heading()!=right:
            self.head.setheading(left)
    def right(self):#4
        if self.head.heading()!=left:
            self.head.setheading(right)        
    def add_tail(self,position):#9
            my_snake=Turtle(shape="square")#9
            my_snake.color(random.choice(colors))#9
            my_snake.penup()#9                      
            my_snake.goto(position)#9
            self.segments.append(my_snake)#9
    def extend(self):#9
        self.add_tail(self.segments[-1].position())