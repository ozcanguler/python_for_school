import csv
import pandas
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
print(datapanda["temp"])