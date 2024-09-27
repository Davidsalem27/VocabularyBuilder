from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QLineEdit, QPushButton, QLabel


class SetTimedQuizzesMenu(QWidget):
    def __init__(self,controller):
        super().__init__()
        self.controller=controller
        self.setWindowTitle("Set a Quiz")
        self.setGeometry(100, 100, 800, 600)
        # self.create_timed_quiz=create_timed_quiz
        # Set up the main layout
        self.layout = QVBoxLayout(self)

        # Dropdown menu
        self.quiz_type = QComboBox()
        self.quiz_type.addItems(["Basic Quiz", "Basic Quiz 2"])
        self.layout.addWidget(QLabel("Select a Quiz:"))
        self.layout.addWidget(self.quiz_type)

        # Entry fields with labels
        self.label1 = QLabel("Set the time interval between quizzes in hours")
        self.entry_time_interval = QLineEdit("3")
        self.label2 = QLabel("Set the number of words per quiz")
        self.entry_num_words = QLineEdit("5")

        # Add the labels and entry fields to the layout
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.entry_time_interval)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.entry_num_words)

        # Horizontal layout for buttons
        button_layout = QHBoxLayout()
        self.button1 = QPushButton("Set Timed Quiz")
        self.button2 = QPushButton("go back")
        self.button1.clicked.connect(self.set_timed_quiz)
        self.button2.clicked.connect(self.close_window)

        button_layout.addWidget(self.button1)
        button_layout.addWidget(self.button2)

        # Add button layout to the main layout
        self.layout.addLayout(button_layout)

    def set_timed_quiz(self):
        self.controller.open_quiz(self.entry_time_interval.text(),
                                  self.entry_num_words.text(),self.quiz_type.currentText())
        self.close()


    def close_window(self):
        self.close()

