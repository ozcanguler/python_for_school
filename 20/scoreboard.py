from turtle import Turtle   #7
ALIGMENT='center'   #7
FONT=('Arial',15,'bold')    #7



class Scoreboard(Turtle):   #7
    def __init__(self): #7
        super().__init__()  #7
        with open("C:/Users/Garavel/Desktop/pythonsil/snake_game/son/data.txt",mode="r") as fileread:
            self.high_score=fileread.read()
            fileread.close()
        self.score=0    #7
        #self.high_score=0
        self.goto(0,270)    #7
        self.color("white") #7
        self.update_scoreboard()    #7
        self.hideturtle()   #7

    def update_scoreboard(self):    #7
        self.clear()
        #self.write(f"Scoreboard:{self.score}" ,align=ALIGMENT,font=FONT)    #7
        self.write(f"Score:{self.score} High Score: {self.high_score}" ,align=ALIGMENT,font=FONT)

    def refresh_score(self):        #7   
        self.score+=1   #7
        #self.clear()    #7
        self.update_scoreboard()    #7
    
    def reset(self):
        with open("C:/Users/Garavel/Desktop/pythonsil/snake_game/son/data.txt",mode="w") as filewrite:            
            if self.score>int(self.high_score):
                self.high_score=self.score
                filewrite.write(f"{self.high_score}")
                filewrite.close()
            self.score=0
            self.update_scoreboard()
    
    def game_over(self):    #8
        self.goto(0,0)
        self.write("Game Over", align=ALIGMENT,font=FONT)

        
        
