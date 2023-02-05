numbers=[1,2,3]
new_numbers=[new_item+1 for new_item in numbers]
print(new_numbers)

name="Ozcan"
new_list=[letter for letter in name]
print(new_list)

newlist1=[]
for i in name:
    newlist1.append(i)
print(newlist1)


range_list=[num*2 for num in range(1,5)]
print(range_list)

names=["Sir Ferguson","Wenger","Mourinho","Guardiola","Ancelotti","Klopp"]
short_names=[name for name in names if len(name)<8]
print(short_names)

upper_names=[name.upper() for name in names if len(name)>8]
print(upper_names)

q_numbers=[1,1,2,3,5,8,13,21,34,55]
square_number=[num*num for num in q_numbers]
print(square_number)

even_number=[num for num in q_numbers if(num%2==0)]
print(even_number)
