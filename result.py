class QuizBrain:
    def __init__(self,q_list):
        self.question_num=0
        self.question_list=q_list
        self.score=0
        
    def next_question(self):
        current_question=self.question_list[self.question_num]
        self.question_num+=1
        user_choice=input(f"Q.{self.question_num}:{current_question.que}(True/False):")
        self.check_answer(user_choice,current_question.ans)
    
    def still_has_question(self):
        return self.question_num < len(self.question_list)
   
    def check_answer(self,user_choice,correct_answer):
        if user_choice.lower() == correct_answer.lower():
            print("you got it right")
            self.score+=1
        else:
            print("you got it wrong")
        print(f"correct answer is {correct_answer}")
        print(f"your current score is :{self.score}/{self.question_num}")
        print("\n")
    
           
