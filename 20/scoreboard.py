from turtle import Turtle   #7
ALIGMENT='center'   #7
FONT=('Arial',15,'bold')    #7
class Scoreboard(Turtle):   #7
    def __init__(self): #7
        super().__init__()  #7
        self.score=0    #7
        self.goto(0,270)    #7
        self.color("white") #7
        self.update_scoreboard()    #7
        self.hideturtle()   #7

    def update_scoreboard(self):    #7
        self.write(f"Scoreboard:{self.score}" ,align=ALIGMENT,font=FONT)    #7

    def refresh_score(self):        #7   
        self.score+=1   #7
        self.clear()    #7
        self.update_scoreboard()    #7
        
        
