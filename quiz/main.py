from question import Question
from questions import questions
from quiz_brain import QuizBrain
from ui import QuizUi

print("\nWelcome to PyQuiz! Make sure you see the game open in the new window.\n")

questions_bank = []
for question in questions:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    questions_bank.append(new_question)

quiz = QuizBrain(questions_bank)
quiz_ui = QuizUi(quiz)

print(f"Thanks for playing! Your score is {quiz.score} out of {quiz.question_number}.")