import tkinter as tk

import ShowWordsMenu

#
# class ManageWordsMenu:
#     def __init__(self, root, controller):
#
#         self.top = tk.Toplevel(root)  # Create a new Toplevel window
#         self.controller=controller
#         self.top.title("Manage the words!")
#         self.top.geometry("600x400")
#
#
#         # Create a label in the new screen
#         label = tk.Label(self.top, text="Enter a word you wish to add or delete:")
#         label.pack(pady=10)
#         # Create a text entry field
#         self.entry = tk.Entry(self.top, width=30)
#         self.entry.pack(pady=5)
#
#         # Create a submit button
#         self.submit_button = tk.Button(self.top, text="Add a new word", command=self.submit_word)
#         self.submit_button.pack(pady=20)  # Add some vertical padding
#         # Create a delete button
#         self.delete_button = tk.Button(self.top, text="delete a word", command=self.delete_word)
#         self.delete_button.pack(pady=20)  # Add some vertical padding
#
#         self.meanings_button = tk.Button(self.top, text="meaning", command=self.get_meanings)
#         self.meanings_button.pack(pady=20)  # Add some vertical padding
#         show_words_button = tk.Button(self.top, text="show all words", command=self.open_show_words_menu)
#         show_words_button.pack(pady=20)  # Add some vertical padding
#     def get_meanings(self):
#         self.controller.get_meanings(self.entry.get())
#         self.entry.delete(0, tk.END)
#     def delete_word(self):
#         self.controller.delete_word( self.entry.get())
#
#         self.entry.delete(0, tk.END)
#
#
#     def submit_word(self):
#         new_word = self.entry.get()
#         if new_word:
#             self.controller.submit_new_word(new_word)
#
#             self.entry.delete(0, tk.END)
#         else:
#             self.output_label.config(text="Please enter a word.")
#
#     def open_show_words_menu(self):
#         show_words_controller=self.controller.open_show_words_menu()
#         ShowWordsMenu.ShowWordsMenu(self.top,show_words_controller)
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
        self.controller.add_new_word(user_input)
        self.output_label.setText(f'Word added to database: {user_input}')

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


