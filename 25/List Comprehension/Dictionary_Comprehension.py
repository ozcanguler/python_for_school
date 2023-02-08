import random
import pandas
artist_dict={"artist":["Tom Hanks","Marlon Brando","Harrison Ford"],
"birth_day":[1956,1924,1942]}
names=["Harry","Ron","Hermione","Draco","Fred","George","Ginny","Vincent","Gregory","Neville","Tom"]
wizard_scores={wizard:random.randint(1,100) for wizard in names}
print(wizard_scores)
passed_wizards={wizard:score for (wizard,score) in wizard_scores.items() if score>=65}
print(passed_wizards)



sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result={word:len(word) for word in sentence.split()}
print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f={day:temp_c*9/5+32 for day,temp_c in weather_c.items()}

print(weather_f)


artist_dataframe=pandas.DataFrame(artist_dict)
print(artist_dataframe)
for(index,row) in artist_dataframe.iterrows():
    if row.artist=="Tom Hanks":
        print(row.birth_day)