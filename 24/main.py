import csv
import pandas
import numpy
'''with open("/Users/Garavel/Desktop/pythonsil/reading_CSVData/weather-data.csv",mode="r") as fileread_weather:
    data=fileread_weather.readlines()
    print(data)'''
temperatures=[]
with open("/Users/Garavel/Desktop/pythonsil/reading_CSVData/weather-data.csv",mode="r") as fileread_weather:
    data=csv.reader(fileread_weather)
    for row in data:        
        print(row)
        if row[1]!="temp":
            temperatures.append(int(row[1]))
    print(temperatures)

datapanda=pandas.read_csv("/Users/Garavel/Desktop/pythonsil/reading_CSVData/weather-data.csv")
print(type(datapanda))
print(datapanda["temp"])

data_dict=datapanda.to_dict()
print(data_dict)

temp_list=datapanda["temp"].to_list()
temp_list1=datapanda["temp"].mean()
temp_list_max=datapanda["temp"].max()
print(f"average temperature: {temp_list1}")
print(f"average temperature: {numpy.average(temp_list)}")
print(f"max temperature: {(temp_list_max)}")
#print(datapanda["condition"])
print(datapanda.condition)
#print(datapanda[datapanda.temp.max()])
#print(datapanda[datapanda["temp"]])
print(datapanda[datapanda.temp.max()==datapanda["temp"]])
monday=datapanda[datapanda.day=="Monday"]
print(monday)
fahrenheit=(monday.temp*1.8)+32
print(monday.temp)
print(fahrenheit)

data_dict={
    "city":["Ankara","Istanbul"],
    "code":[6,34]
}
data_city=pandas.DataFrame(data_dict)
data_city.to_csv("new_data_city.csv")