from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.canvas = Canvas(width=300, height=250)
        self.canva_text = self.canvas.create_text(150, 125,
                                                  fill="black",
                                                  text="Hi",
                                                  width=280,
                                                  font=("arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # self.canvas

        # Labels
        self.label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.label.grid(row=0, column=1)

        # Buttons
        self.true_img = PhotoImage(file="images/true.png")
        self.true_button = self.button = Button(image=self.true_img, highlightthickness=0, command=self.true_pressed)
        self.button.grid(row=2, column=0)

        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = self.button = Button(image=self.false_img, highlightthickness=0, command=self.false_pressed)
        self.button.grid(row=2, column=1)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canva_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canva_text, text="You've reached the end of the Quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, variable):
        if variable:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)


# self.canvas.config(bg="white")