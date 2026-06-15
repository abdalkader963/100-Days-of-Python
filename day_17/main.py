from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
qustion_bank=[]
for qus in question_data:
    t=qus["question"]
    a=qus["correct_answer"]
    qa=Question( t , a)
    qustion_bank.append(qa)
quiz=QuizBrain(qustion_bank)
while quiz.still_has_questions():
    quiz.next_qustion()
print(f"You've completed the quiz\nYour final score was: {quiz.score}/{quiz.number_of_qustions}")    
    

