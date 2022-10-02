
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
#list_position=list(str(position))
#print(type(position))
list_position1=int(position[1])
list_position2=int(position[0])

print(map[list_position1-1][list_position2-1])
map[list_position1-1][list_position2-1]='X'


print(f"{row1}\n{row2}\n{row3}")