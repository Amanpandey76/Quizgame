from data import my_data
from main import Question
from result import QuizBrain
info=[]
for data in my_data:
    question_1=data["text"]
    answer_1=data["answer"]
    reply=Question(question_1,answer_1)
    info.append(reply)
    
quiz=QuizBrain(info)
while quiz.still_has_question():
    quiz.next_question()
    
print("you have completed the quiz ")
print(f"your final score is :- {quiz.score}/{quiz.question_num}")