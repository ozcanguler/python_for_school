from data import question_data,qquestion_data
from quiz_brain import QuizBrain
class Question():                       #1
    def __init__(self,text,answer):
        self.text=text
        self.answer=answer
'''q1=Question("5+3=7","False")
a=input(f"{q1.text} <=> True or False ?\n")
if q1.answer==a:
    print("CongratsF")'''
question_bank=[]                #3
for i in qquestion_data:     #2
    q_text=i["question"]
    q_answer=i["correct_answer"]
    new_question= Question(q_text,q_answer)
    question_bank.append(new_question)
print(question_bank[0].text)

quiz=QuizBrain(question_bank)       #4
while quiz.next_question():     
    quiz.question()
print(f"Completed the quiz\nYour score is:{quiz.score}/{quiz.question_number}")
