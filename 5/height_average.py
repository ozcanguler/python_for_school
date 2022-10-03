student_heights = input("Input a list of student heights ").split()
sum_student_heights=0
num_student=0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  sum_student_heights+=student_heights[n]
  num_student+=1
avg_student_heights=sum_student_heights/num_student
print(round(avg_student_heights))