from question import Question
from questions import questions
from quiz_brain import QuizBrain
from ui import QuizUi

print("\nWelcome to PyQuiz! Answer 10 questions correctly and be considered a genius!\n")

question_bank = []
for question in questions:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizUi(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("Thanks for playing!")
print(f"Your final score is {quiz.score} out of {quiz.question_number}")