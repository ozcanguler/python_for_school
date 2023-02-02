import csv
import pandas
import numpy
'''with open("/Users/Garavel/Desktop/pythonsil/reading_CSVData/Central-Park-Squirrel-Census-Squirrel-Data.csv",mode="r") as fileread_central:
    data=csv.reader(fileread_central)
    for row in data:        
        print(row)
        if row[1]!="temp":
            fileread_central.append(int(row[1]))
    print(fileread_central)'''

datapanda=pandas.read_csv("/Users/Garavel/Desktop/pythonsil/reading_CSVData/Central-Park-Squirrel-Census-Squirrel-Data.csv")

gray=len(datapanda[datapanda["Primary Fur Color"]=="Gray"])
print("Gray: ",gray)
cinnamon=len(datapanda[datapanda["Primary Fur Color"]=="Cinnamon"])
print("Cinnamon: ",cinnamon)
black=len(datapanda[datapanda["Primary Fur Color"]=="Black"])
print("Black: ",black)

data_dict={
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[gray,cinnamon,black]
}
data_fur=pandas.DataFrame(data_dict)
data_fur.to_csv("fur_color_count.csv")