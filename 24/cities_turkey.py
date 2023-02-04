import turtle
import pandas

matching_city=[]
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

while len(matching_city)<81:
    answer_city=screen.textinput(title=f"{len(matching_city)}/81 Cities Correct", prompt="What's another city name?").title() #title first letter capitalized
    if answer_city=="Exit":
        missing_cities=[]
        for city in cities:
                if city not in matching_city:
                        missing_cities.append(city)
        new_data=pandas.DataFrame(missing_cities)
        new_data.to_csv("cities_to_learn.csv")
        exit()
    if answer_city in cities:
        matching_city.append(answer_city)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data= datapanda[datapanda.city==answer_city]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_city)


turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()



#screen.exitonclick()