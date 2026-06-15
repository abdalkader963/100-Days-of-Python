class QuizBrain:
    def __init__(self, q_list):
        self.qustion_number = 0
        self.score = 0
        self.qustion_list = q_list
        self.number_of_qustions = len(self.qustion_list)

    def still_has_questions(self):
        return self.qustion_number < self.number_of_qustions

    def next_qustion(self):
        current_question = self.qustion_list[self.qustion_number]
        self.qustion_number += 1
        user_in = input(f"Q.{self.qustion_number}: {current_question.text}. (True/False)? ").title()
        self.check_answer(user_in, current_question.answer)
        
    def check_answer(self, user_in, answer):
        if user_in == answer:
            print("You got it right! ")
            self.score += 1
        else:
            print("That's wrong! ")  
            
        print(f"Your current score is: {self.score}/{self.qustion_number}")
        print(f"The correct answer was: {answer}\n") 