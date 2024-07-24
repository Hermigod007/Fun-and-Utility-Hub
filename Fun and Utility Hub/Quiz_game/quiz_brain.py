class QuizBrain:
    def __init__(self, ques_list):
        self.question_no = 0
        self.ques_list = ques_list
        self.score = 0

    def still_has_questions(self):
        if len(self.ques_list) > self.question_no:
            return True
        else:
            return False

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Your answer was correct")
            self.score += 1
        else:
            print(f"Your answer was wrong and the correct answer was {correct_answer}")
            print("Thank you for playing the game")
            print(f"Your total score was {self.score} out of {len(self.ques_list)}")
            exit()

    def next_question(self):
        current_question = self.ques_list[self.question_no]
        self.question_no += 1
        user_answer = input(f"Q.{self.question_no} {current_question.text} (True or false): ")
        correct_answer = current_question.answer
        self.check_answer(user_answer, correct_answer)

