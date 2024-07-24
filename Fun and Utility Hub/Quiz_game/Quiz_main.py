from .Quiz_data import data
from .question_model import Question
from .quiz_brain import QuizBrain

class QuizGame:
    def __init__(self):
        self.question_bank = []
        self.load_questions()
        self.quiz = QuizBrain(self.question_bank)

    def load_questions(self):
        size = len(data)
        for i in range(size):
            ques = data[i]["text"]
            ans = data[i]["answer"]
            new_question = Question(ques, ans)
            self.question_bank.append(new_question)

    def start(self):
        while self.quiz.still_has_questions():
            self.quiz.next_question()


