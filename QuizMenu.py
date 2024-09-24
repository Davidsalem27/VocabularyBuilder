import tkinter as tk

import BasicQuizMenu
import QuizController


class QuizMenu:
    """
    the view aspect of the quiz, represents the window of the quiz
    """
    def __init__(self, root, controller):
        self.top = tk.Toplevel(root)
        self.controller = controller
        self.create_quiz_menu()

    def create_quiz_menu(self):
        self.top.title("this is the quiz menu!")
        self.top.geometry("600x400")
        manage_words_button = tk.Button(self.top, text="start basic quiz", command=self.open_basic_quiz)
        manage_words_button.pack(pady=20)  # Add some vertical padding

    def open_basic_quiz(self):
        basic_quiz_controller=self.controller.open_basic_quiz()
        BasicQuizMenu.BasicQuizMenu(self.top,basic_quiz_controller)



