
import ShowWordsMenu
import Constants as c
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel

class ManageWordsMenu(QWidget):
    def __init__(self,controller, create_show_all_words):
        super().__init__()
        self.controller=controller
        self.create_show_all_words=create_show_all_words
        self.setWindowTitle('User Input Example')
        self.setGeometry(400, 100, 800, 1000)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.show_words_menu=None
        # Input field for user input
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText('Enter word here...')
        layout.addWidget(self.input_field)
        self.input_field.setFixedSize(600, 100)
        self.input_field.setFont(c.BUTTON_FONT)
        # Button to process the input
        self.add_word_botton = QPushButton('Add word', self)
        self.add_word_botton.clicked.connect(self.add_word)
        layout.addWidget(self.add_word_botton)
        self.add_word_botton.setFixedSize(600, 100)
        self.add_word_botton.setFont(c.BUTTON_FONT)
        # Button to clear the input field
        self.clear_button = QPushButton('Remove word', self)
        self.clear_button.clicked.connect(self.remove_word)
        layout.addWidget(self.clear_button)
        self.clear_button.setFont(c.BUTTON_FONT)
        self.clear_button.setFixedSize(600, 100)
        # Button to call another function
        self.show_all_words_button = QPushButton('Show all words', self)
        self.show_all_words_button.clicked.connect(self.open_show_all_words)

        layout.addWidget(self.show_all_words_button)
        self.show_all_words_button.setFont(c.BUTTON_FONT)

        self.show_all_words_button.setFixedSize(600, 100)
        self.show_words_menu=None
        self.delete_all_words_button = QPushButton('Delete all the words', self)
        self.delete_all_words_button.clicked.connect(self.delete_all_words)
        layout.addWidget(self.delete_all_words_button)
        self.delete_all_words_button.setFont(c.BUTTON_FONT)

        self.delete_all_words_button.setFixedSize(600, 100)
        self.load_local_button = QPushButton('Load From local file', self)
        self.load_local_button.clicked.connect(self.load_local_file)
        layout.addWidget(self.load_local_button)
        self.load_local_button.setFixedSize(600, 100)
        self.load_local_button.setFont(c.BUTTON_FONT)

        # Label to display output


        self.output_label = QLabel('', self)
        layout.addWidget(self.output_label)
        self.output_label.setFixedSize(400, 100)
        self.output_label.setFont(c.BUTTON_FONT)

        self.setLayout(layout)

    def delete_all_words(self):
        self.controller.delete_all_words()
    def load_local_file(self):
        text=self.controller.load_local_file()
        self.output_label.setText(text)

    def add_word(self):
        user_input = self.input_field.text()
        text=self.controller.add_new_word(user_input)
        self.output_label.setText(text)
        self.input_field.clear()
    def remove_word(self):
        user_input = self.input_field.text()
        text=self.controller.delete_word(user_input)
        self.output_label.setText(text)
        self.input_field.clear()

    def open_show_all_words(self):
        # Example function that can be called

        self.show_words_menu=self.create_show_all_words()
        self.show_words_menu.show()



