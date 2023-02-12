def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
add(1,2,3)
#keywordarguments
def calculate(n,**kwargs):
    print(type(kwargs))
    print(kwargs)
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)
calculate(2,add=3,multiply=5)

class Car:
    def __init__(self,**kw):
        self.make=kw["make"]
        self.model=kw["model"]
        self.colour=kw["colour"]
        self.seats=kw["seats"]
my_car=Car(make="Nissan",model="GT-R",colour="red",seats=2)
print(my_car.make,my_car.model,my_car.colour,my_car.seats)