import html

class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = questions_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        self.current_question = self.questions_list[self.question_number]
        self.question_number += 1
        question_text = html.unescape(self.current_question.text)
        return f"{self.question_number}: {question_text}"

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
