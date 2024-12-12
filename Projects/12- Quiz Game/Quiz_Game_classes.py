from Quiz_Game_data import *

class Question:
    
    def __init__(self, question, answer):
        
        self.question = question
        self.answer = answer

class Question_Bank:
    
    def __init__(self, question_list):
        
        self.question_no = 0
        self.score = 0
        self.question_list = question_list
        
    def ask_question(self):
        
        current_q = self.question_list[self.question_no].question
        current_a = self.question_list[self.question_no].answer
        print(f"Q.{self.question_no+1}: {current_q} (True/False)?")
        def check_ans(self):
            ans = (input("Type your answer: ")).title()
            if ans == "True" or ans == "False":
                if ans == current_a:
                    print("You got it right!!")
                    self.score += 1
                else:
                    print("That's wrong.")
            else:
                print(f"Wrong Input. Type Again")
                check_ans(self)
        check_ans(self)
        print(f"The correct answer was: {current_a}")
        print(f"Current Score: {self.score}/{self.question_no+1}\n")
        self.question_no += 1
        
    def end_of_game(self):
        
        total_ques_no = len(self.question_list)
        return self.question_no == total_ques_no
        