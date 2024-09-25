import tkinter as tk
from tkinter import font
# class ShowWordsMenu:
#
#     def __init__(self, root, controller):
#         self.top = tk.Toplevel(root)  # Create a new Toplevel window
#         self.controller = controller
#         self.top.title("List of Words")
#         self.top.geometry("600x400")
#         self.list_of_words = self.controller.get_all_words()
#         self.meanings_font = font.Font(size=16)
#         self.word_listbox = tk.Listbox(self.top, width=50, height=50)
#         self.word_listbox.pack(pady=10)
#         self.create_list()
#
#
#     def create_list(self):
#
#         for word in self.list_of_words:
#             self.word_listbox.insert(tk.END, word)
#         self.word_listbox.bind('<<ListboxSelect>>', self.show_meaning)
#
#     def show_meaning(self, event):
#         selected_index = self.word_listbox.curselection()
#         if selected_index:
#             word = self.word_listbox.get(selected_index)
#             # Get the meaning of the selected word
#             meaning = self.controller.get_meaning(word)
#             if meaning:
#                 self.open_meaning_window(word, meaning)
#
#     def open_meaning_window(self, word, meanings):
#         # Create a new window
#         meanings_window = tk.Toplevel(self.top)
#         meanings_window.title(word)
#         meanings_window.geometry("800x600")
#
#         for index, (meaning, example) in enumerate(meanings):
#             meaning_label = tk.Label(meanings_window, text=f"{index + 1}. {meaning}", wraplength=300, justify="left",
#                                      font=self.meanings_font)
#             # meaning_label.pack(anchor="w", padx=10, pady=(10, 0))  # Add some padding
#
#             # Create a label for the example, indented
#             meaning_label.pack(pady=20)
#             if example:
#
#                 example_label = tk.Label(meanings_window, text=f"   Example: {example}", wraplength=300, justify="left",
#                                      font=self.meanings_font)
#                 example_label.pack(pady=20, padx=30)


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QLabel, QPushButton, QScrollArea


class ShowWordsMenu(QWidget):
    def __init__(self,controller):
        super().__init__()
        self.controller=controller
        self.setWindowTitle('Word List')
        self.setGeometry(100, 100, 800, 600)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Create a scroll area for the word list
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        # Create a widget to hold the QListWidget
        list_widget_container = QWidget()
        list_layout = QVBoxLayout(list_widget_container)

        # List widget to display words
        self.word_list = QListWidget(self)
        self.word_list.addItems(self.controller.get_all_words())  # get the words
        self.word_list.itemDoubleClicked.connect(self.open_word_detail)  # Connect double-click to method

        list_layout.addWidget(self.word_list)  # Add the QListWidget to the layout
        list_widget_container.setLayout(list_layout)  # Set the layout for the container

        scroll_area.setWidget(list_widget_container)  # Set the container as the widget of the scroll area
        layout.addWidget(scroll_area)  # Add the scroll area to the main layout

        self.setLayout(layout)

    def open_word_detail(self, item):
        word = item.text()  # Get the word from the clicked item
        meanings = self.controller.get_meaning(word)
        self.detail_window = WordMeaningWindow(word, meanings)  # Create a new window for the word
        self.detail_window.show()  # Show the new window
class WordMeaningWindow(QWidget):
    def __init__(self, word :str,meanings):
        super().__init__()
        self.setWindowTitle('Word Detail')
        self.setGeometry(200, 200, 300, 150)
        self.word=word
        self.meanings=meanings
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel(f'Details for: {self.word}'))  # Display the word details
        self.setLayout(layout)
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_content = QWidget()  # Create a content widget for the scroll area
        scroll_layout = QVBoxLayout(scroll_content)

        # Adding meanings and examples to the layout
        for index, (meaning, example) in enumerate(self.meanings):
            meaning_label = QLabel(f"{index + 1}. {meaning}", self)
            meaning_label.setWordWrap(True)
            scroll_layout.addWidget(meaning_label)

            if example:
                example_label = QLabel(f"   Example: {example}", self)
                example_label.setWordWrap(True)
                scroll_layout.addWidget(example_label)

            # Add spacing between meanings
            scroll_layout.addSpacing(20)

        scroll_area.setWidget(scroll_content)  # Set the content widget in the scroll area
        layout.addWidget(scroll_area)  # Add the scroll area to the main layout

        self.setLayout(layout)
