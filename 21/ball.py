from turtle import Turtle
class Ball(Turtle): 
    def __init__(self): 
        super().__init__() 
        self.shape("circle")    
        self.penup()   
        self.shapesize(stretch_len=0.5,stretch_wid=0.5) 
        self.color("purple")  
        self.x_move=10
        self.y_move=5
        self.move_speed=0.05    
    def move(self): 
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)
    def bounce_y(self):
        self.y_move*=-1       
    def bounce_x(self):
        self.x_move*=-1 
        self.move_speed*=0.9
    def reset_ball_p(self):
        self.move_speed=0.05
        self.goto(0,0)
        self.bounce_x()
    def speed_increase(self):
        self.x_move+=1     

        
          
