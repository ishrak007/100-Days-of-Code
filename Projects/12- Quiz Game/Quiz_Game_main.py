from Quiz_Game_data import *
from Quiz_Game_classes import *

question_list = [] 
for i in question_data:
    current_q = i["text"]
    current_a = i["answer"]
    question = Question(current_q, current_a)
    question_list.append(question)
        
question_bank = Question_Bank(question_list)
game_end = False
print(logo)

while not game_end:
    
    question_bank.ask_question()
    end = question_bank.end_of_game()
    if end:
        game_end = True
        print(f"\nYour Final Score: {question_bank.score}/{question_bank.question_no}")
