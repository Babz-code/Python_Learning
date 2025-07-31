#from main import question_bank
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_question = input(f"Q. {self.question_number}: {current_question.text} (True/False)?")
        self.check_answer(user_question, current_question.answer)

    def check_answer(self, user_question, correct_answer):
        if user_question.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")

        else:
            print("You're wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
