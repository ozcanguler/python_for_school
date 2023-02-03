import turtle
import pandas

#cities=[]
matching_city=[]
screen=turtle.Screen()
screen.setup(1200, 800)
screen.title("Cities of Turkey")
image="/Users/Garavel/Desktop/pythonsil/reading_CSVData/Turkey_cities.gif"
screen.addshape(image)
turtle.shape(image)

datapanda=pandas.read_csv("/Users/Garavel/Desktop/pythonsil/reading_CSVData/turkey_data_city.csv")
cities=datapanda.city.to_list()
#print(datapanda["city"])
#total_city=len(datapanda["city"])
#data_dict=datapanda.to_dict()
#print(data_dict)
#print(total_city)

def get_mouse_click_coor(x, y):
        print(x, y)

while len(matching_city)<50:
    answer_city=screen.textinput(title=f"{len(matching_city)}/50 States Correct", prompt="What's another city name?").title()
    if answer_city in cities:
        matching_city.append(answer_city)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data= datapanda[datapanda.city==answer_city]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_city)

#turtle.onscreenclick(get_mouse_click_coor)
#turtle.mainloop()



screen.exitonclick()