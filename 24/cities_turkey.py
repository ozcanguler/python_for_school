import turtle
import pandas

screen=turtle.Screen()
screen.setup(1200, 800)
screen.title("Cities of Turkey")
image="/Users/Garavel/Desktop/pythonsil/reading_CSVData/Turkey_cities.gif"
screen.addshape(image)
turtle.shape(image)

datapanda=pandas.read_csv("/Users/Garavel/Desktop/pythonsil/reading_CSVData/turkey_data_city.csv")
cities=datapanda.city.to_list()

def get_mouse_click_coor(x, y):
        print(x, y)

for i in range(81):        
        data_dict=datapanda.to_dict()
        state_data= datapanda[datapanda.city==cities[i]]
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()     
        t.goto(int(state_data.x),int(state_data.y))
        t.write(cities[i])

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()



#screen.exitonclick()