student_scores=input("Input a list of student scores ").split()
for n in range(0,len(student_scores)):
    student_scores[n]=int(student_scores[n])
'''   
max=student_scores[0]
for x in range(0,len(student_scores)):  
    if(x+1==len(student_scores)):
        if(max<student_scores[x]):
            print(student_scores[x])
        else:
            print(max)  
    else:
        if(max<student_scores[x+1]):
            max=student_scores[x+1]          
'''
highest_score=0
for score in student_scores:
    if(score>highest_score):
        highest_score=score
print(f"The highest score in the class is: {highest_score}")