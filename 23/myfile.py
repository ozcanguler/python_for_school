'''file=open("C:/Users/Garavel/Desktop/pythonsil/ORWFiles/hello.txt")
contents=file.read()
print(contents)
print(file.closed)
file.close()
print(file.closed)'''

with open("C:/Users/Garavel/Desktop/pythonsil/ORWFiles/hello.txt") as fileread:
    contents=fileread.read()
print(contents)
print(fileread.closed)
fileread.close()
print(fileread.closed)

with open("C:/Users/Garavel/Desktop/pythonsil/ORWFiles/hello.txt",mode="w") as filewrite:
    filewrite.write("Who wants to play a game?") 

with open("C:/Users/Garavel/Desktop/pythonsil/ORWFiles/hello.txt",mode="a") as fileappend:
    fileappend.write("\nIt's time to play hide and seek!") 

with open("C:/Users/Garavel/Desktop/pythonsil/ORWFiles/newfile.txt",mode="w") as fileappend:
    fileappend.write("Welcome to the my world |o-o|")