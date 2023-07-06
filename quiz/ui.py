from tkinter import *
# Label, Canvas, PhotoImage and Button are built-in classes from tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizUi:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk() # tkinter initializing
        self.window.title("PyQuiz")
        # self.window.geometry("700x350")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg='white', bg=THEME_COLOR) # creates text area
        self.score_label.grid(row=0, column=1) # location of area

        self.canvas = Canvas(width=300, height=250, bg='white') # creates game field
        self.question_text = self.canvas.create_text(150, 125, width=280, text='hello text', fill=THEME_COLOR, font=('Arial', 20, 'italic')) # coords of text center, text itself, text width, color, font
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_button_img = PhotoImage(file='quiz/images/true.png')
        self.true_button = Button(image=true_button_img, highlightthickness=0, command=self.true_btn_pressed)
        self.true_button.grid(row=2, column=0)

        false_button_img = PhotoImage(file='quiz/images/false.png')
        self.false_button = Button(image=false_button_img, highlightthickness=0, command=self.false_btn_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop() # constantly runs which helps update UI on change, nothing after .mainloop is read

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text, text='Thanks for playing!')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true_btn_pressed(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def false_btn_pressed(self):
        self.give_feedback(self.quiz.check_answer('False')) # shorter implementation of what's in true_btn_pressed method

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)