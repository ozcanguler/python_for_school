
with open("/Users/Garavel/Desktop/pythonsil/List Comprehension/file1.txt") as file1:
    file1_data=file1.readlines()
with open("/Users/Garavel/Desktop/pythonsil/List Comprehension/file2.txt") as file2:
    file2_data=file2.readlines()

new_list=[int(num) for num in file1_data if num in file2_data]
print(new_list)