import tkinter as tk

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QSlider

import BasicQuizController
import BasicQuizMenu
import QuizMenuController


# class QuizMenu:
#     """
#     the view aspect of the quiz, represents the window of the quiz
#     """
#     def __init__(self, root, controller):
#         self.top = tk.Toplevel(root)
#         self.controller = controller
#         self.create_quiz_menu()
#
#     def create_quiz_menu(self):
#         self.top.title("this is the quiz menu!")
#         self.top.geometry("600x400")
#         manage_words_button = tk.Button(self.top, text="start basic quiz", command=self.open_basic_quiz)
#         manage_words_button.pack(pady=20)  # Add some vertical padding
#
#     def open_basic_quiz(self):
#         basic_quiz_controller=self.controller.open_basic_quiz()
#         BasicQuizMenu.BasicQuizMenu(self.top,basic_quiz_controller)

class QuizMenu(QWidget):
    def __init__(self,controller,create_basic_quiz,create_timed_quiz_menu):
        super().__init__()
        self.set_menu = None
        self.create_timed_quiz_menu=create_timed_quiz_menu
        self.create_basic_quiz=create_basic_quiz
        self.setWindowTitle('Quiz Menu')
        self.setGeometry(100, 100, 300, 200)
        self.controller=controller
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Label to display output
        self.output_label = QLabel('Click a button to see the action.', self)
        layout.addWidget(self.output_label)

        # Button 1
        self.button1 = QPushButton('Start Basic Quiz', self)
        self.button1.clicked.connect(self.open_basic_quiz_menu)
        layout.addWidget(self.button1)

        # Button 2
        self.button2 = QPushButton('Start Basic Quiz 2', self)
        self.button2.clicked.connect(self.function2)
        layout.addWidget(self.button2)

        # Button 3
        self.button3 = QPushButton('Set Timed Quiz', self)
        self.button3.clicked.connect(self.open_set_time_quiz)
        layout.addWidget(self.button3)



        # Connect slider value change to a method
        self.setLayout(layout)

    def open_basic_quiz_menu(self):
        self.basic_quiz=self.create_basic_quiz()
        self.basic_quiz.show()

    def function2(self):
        self.output_label.setText('Function 2 was called!')

    def open_set_time_quiz(self):
        self.set_menu=self.create_timed_quiz_menu()
        self.set_menu.show()

