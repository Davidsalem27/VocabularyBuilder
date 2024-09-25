
import ShowWordsMenu

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel

class ManageWordsMenu(QWidget):
    def __init__(self,controller):
        super().__init__()
        self.controller=controller
        self.setWindowTitle('User Input Example')
        self.setGeometry(100, 100, 400, 300)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Input field for user input
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText('Enter word here...')
        layout.addWidget(self.input_field)

        # Button to process the input
        self.process_button = QPushButton('Add word', self)
        self.process_button.clicked.connect(self.add_word)
        layout.addWidget(self.process_button)

        # Button to clear the input field
        self.clear_button = QPushButton('Remove word', self)
        self.clear_button.clicked.connect(self.remove_word)
        layout.addWidget(self.clear_button)

        # Button to call another function
        self.show_all_words_button = QPushButton('Show all words', self)
        self.show_all_words_button.clicked.connect(self.show_all_words)
        layout.addWidget(self.show_all_words_button)

        self.delete_all_words_button = QPushButton('Delete all the words', self)
        self.delete_all_words_button.clicked.connect(self.delete_all_words)
        layout.addWidget(self.delete_all_words_button)

        self.load_local_button = QPushButton('Load From local file', self)
        self.show_all_words_button.clicked.connect(self.load_local_file)
        layout.addWidget(self.load_local_button)

        # Label to display output
        self.output_label = QLabel('', self)
        layout.addWidget(self.output_label)

        self.setLayout(layout)

    def delete_all_words(self):
        self.controller.delete_all_words()
    def load_local_file(self):
        self.controller.load_local_file()

    def add_word(self):
        user_input = self.input_field.text()
        text=self.controller.add_new_word(user_input)
        self.output_label.setText(text)
        self.input_field.clear()
    def remove_word(self):
        user_input = self.input_field.text()
        self.controller.delete_word(user_input)
        self.output_label.setText(f'Word removed from database: {user_input}')
        self.input_field.clear()

    def show_all_words(self):
        # Example function that can be called
        show_words_controller=self.controller.open_show_words_menu()
        self.show_words_menu=ShowWordsMenu.ShowWordsMenu(show_words_controller)
        self.show_words_menu.show()


