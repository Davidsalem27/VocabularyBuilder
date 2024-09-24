import tkinter as tk

import customtkinter

import Constants as c
import ManageWordsMenu
import QuizMenu
import ShowWordsMenu
import customtkinter as ctk

class MainMenu:

    def __init__(self, root : tk.Tk, controller, start_quizzing_callback):

        self.start_quizzing_callback = start_quizzing_callback
        self.root=root

        self.controller = controller
        self.create_main_menu()
        self.start_quizzing_callback=start_quizzing_callback
    # def set_mediator(self, mediator):
    #     self.mediator = mediator

    def create_main_menu(self):
        self.root.title(c.TITLE_MAIN_MENU)
        self.root.geometry(c.SIZE_MAIN_MENU)

        # Create a button
        manage_words_button = tk.Button(self.root, text="Manage words", command=self.open_words_menu)
        manage_words_button.pack(pady=20)  # Add some vertical padding
        # Create a show all words button
        # show_words_button = tk.Button(self.root, text="show all words", command=self.open_show_words_menu)
        # show_words_button.pack(pady=20)  # Add some vertical padding

        quiz_menu_button = tk.Button(self.root, text="Quiz yourself right now!", command=self.open_quiz_menu)
        quiz_menu_button.pack(pady=20)  # Add some vertical padding
        quiz_menu_button = tk.Button(self.root, text="Turn on quiz mode", command=self.start_quizzing_callback)
        quiz_menu_button.pack(pady=20)  # Add some vertical padding

    def open_quiz_menu(self):
        quiz_controller=self.controller.open_quiz_menu()
        QuizMenu.QuizMenu(self.root,quiz_controller)

    def open_words_menu(self):
        show_words_controller=self.controller.open_words_menu()
        ManageWordsMenu.ManageWordsMenu(self.root, show_words_controller)


    # def open_show_words_menu(self):
    #     show_words_controller=self.controller.open_show_words_menu()
    #     ShowWordsMenu.ShowWordsMenu(self.root,show_words_controller)
