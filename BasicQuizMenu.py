import tkinter as tk
from tkinter import font

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QHBoxLayout, QPushButton, QLabel

SIZE_QUIZ = 5

class BasicQuizMenu(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.current_window_index = 0
        self.setWindowTitle("Basic Quiz")
        self.setGeometry(100, 100, 800, 800)
        self.current_word=""
        self.current_meaning=None
        self.definitions = self.controller.get_n_definitions(SIZE_QUIZ)
        # self.word_label = QLabel("", self)
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)

        # Create a scroll area for meanings and examples
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget()  # Create a content widget for the scroll area
        self.scroll_layout = QVBoxLayout(self.scroll_content)

        self.layout.addWidget(self.scroll_area)
        self.scroll_area.setWidget(self.scroll_content)

        # Create navigation buttons
        button_layout = QHBoxLayout()

        self.prev_button = QPushButton("Previous", self)
        self.prev_button.clicked.connect(self.prev_window)
        button_layout.addWidget(self.prev_button)

        self.next_button = QPushButton("Next", self)
        self.next_button.clicked.connect(self.next_window)
        button_layout.addWidget(self.next_button)

        self.reveal_button = QPushButton("Reveal meaning!", self)
        self.reveal_button.clicked.connect(self.reveal_meaning)
        button_layout.addWidget(self.reveal_button)

        self.easy_button = QPushButton("Easy", self)
        self.easy_button.clicked.connect(lambda: self.easy_word(self.current_word))
        button_layout.addWidget(self.easy_button)

        self.hard_button = QPushButton("Hard", self)
        self.hard_button.clicked.connect(lambda: self.hard_word(self.current_word))
        button_layout.addWidget(self.hard_button)

        self.layout.addLayout(button_layout)

        self.create_window()
        self.show()

    def create_window(self):
        # Clear previous widgets in scroll area
        for i in reversed(range(self.scroll_layout.count())):
            widget = self.scroll_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        word_label = QLabel("", self)
        self.current_word = self.definitions[self.current_window_index][0]
        word_label.setText(self.current_word)

        # Create word label
        # self.word_label = QLabel(self.current_word, self)

        word_label.setStyleSheet("font-size: 30px;")
        self.scroll_layout.addWidget(word_label,alignment=Qt.AlignCenter)


    def create_labels_meanings_examples(self):
        # Create the labels for meaning
        current_meaning = self.definitions[self.current_window_index][1]

        self.current_word = self.definitions[self.current_window_index][0]
        self.label_meanings_examples = []
        for index, (meaning, example) in enumerate(current_meaning):
            meaning_label = QLabel(f"{index + 1}. {meaning}", self)
            meaning_label.setWordWrap(True)
            meaning_label.setStyleSheet("font-size: 16px;")
            self.scroll_layout.addWidget(meaning_label)
            if example:
                example_label = QLabel(f"   Example: {example}", self)
                example_label.setWordWrap(True)
                example_label.setStyleSheet("font-size: 16px;")
                self.scroll_layout.addWidget(example_label)
                self.label_meanings_examples.append((meaning_label, example_label))
            else:
                self.label_meanings_examples.append((meaning_label, None))

    def reveal_meaning(self):
        current_meaning = self.definitions[self.current_window_index][1]


        for index, (meaning, example) in enumerate(current_meaning):
            meaning_label = QLabel(f"{index + 1}. {meaning}", self)
            meaning_label.setWordWrap(True)
            meaning_label.setStyleSheet("font-size: 16px;")
            self.scroll_layout.addWidget(meaning_label)
            if example:
                example_label = QLabel(f"   Example: {example}", self)
                example_label.setWordWrap(True)
                example_label.setStyleSheet("font-size: 16px;")
                self.scroll_layout.addWidget(example_label)




    def easy_word(self, word):
        self.controller.update_word_easy(word)

    def hard_word(self, word):
        self.controller.update_word_hard(word)

    def next_window(self):
        if self.current_window_index < len(self.definitions) - 1:
            self.current_window_index += 1
            self.create_window()

    def prev_window(self):
        if self.current_window_index > 0:
            self.current_window_index -= 1
            self.create_window()