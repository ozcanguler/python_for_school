from turtle import Turtle
import random
colors=["red","orange","yellow","green","blue","purple"]
starting_move_distance=5
move_increment=10


class Cars:
    def __init__(self): 
        self.all_cars=[]
        self.car_speed=starting_move_distance

    def create_car(self):
        create_car_chance=random.randint(1,6)
        if(create_car_chance==1):
            new_car=Turtle("square")
            new_car.color(random.choices(colors))
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.goto(200,random.randint(-250,250))
            self.all_cars.append(new_car)
    def go_left(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed+=move_increment       

    '''class Cars(Turtle):
        def __init__(self): 
            super().__init__()
            self.all_cars=[]
            

        def create_car(self):
            self.shape("square")
            self.color(random.choices(colors))
            self.shapesize(stretch_wid=1,stretch_len=2)
            self.penup()
            self.goto(200,random.randint(-250,250))
            self.all_cars.append(self)
        def go_left(self): 
            self.forward(move_increment)'''