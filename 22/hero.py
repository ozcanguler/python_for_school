from turtle import Turtle
starting_position=(0,-280)
move_distance=10
finish_ycor=280

class Hero(Turtle):
    def __init__(self): 
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start_position()
        
    def go_up(self): 
        self.forward(move_distance)

    def go_to_start_position(self):
        self.goto(starting_position)
    def finish_line(self):
        if self.ycor()>finish_ycor:
            return True
        else:
            return False