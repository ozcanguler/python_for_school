from turtle import Turtle   
ALIGMENT='center'   
FONT=('Arial',45,'bold')    
class Scoreboard(Turtle):   
    def __init__(self): 
        super().__init__()  
        self.score=0    
        self.goto(100,200)    
        self.color("white")
        self.penup()
        self.hideturtle() 
        self.l_score=0
        self.r_score=0
        self.update_scoreboard()      

    def update_scoreboard(self):
        self.clear() 
        self.goto(-100,230)    
        self.write(self.l_score ,align=ALIGMENT,font=FONT)
        self.goto(100,230)    
        self.write(self.r_score ,align=ALIGMENT,font=FONT)    

    def l_point(self):          
        self.l_score+=1      
        self.update_scoreboard()   
    def r_point(self):          
        self.r_score+=1            
        self.update_scoreboard()
    '''def game_over(self):    
        self.goto(0,0)
        self.write("Game Over", align=ALIGMENT,font=FONT)'''