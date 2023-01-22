from turtle import Turtle
positions=[(0,0),(-20,0),(-40,0)]#1
move=20
class Snake:
    def __init__(seif):
        seif.segments=[]
        seif.createSnake()
    def createSnake(self):
        for i in positions:#1
            my_snake=Turtle(shape="square")#1
            my_snake.penup()#2
            my_snake.goto(i)#1
            my_snake.color("white")#1
            self.segments.append(my_snake)#2
    def move(self):
        for s in range(len(self.segments)-1,0,-1):#3
            new_x=self.segments[s-1].xcor()#3
            new_y=self.segments[s-1].ycor()#3
            self.segments[s].goto(new_x,new_y)#3
        self.segments[0].forward(move) #3
        self.segments[0].left(30)   #3  