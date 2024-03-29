from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=0.5)
        self.color("White")
        self.penup()
        self.goto(position)
    def pong_up(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(), new_y)
    def pong_down(self):
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)