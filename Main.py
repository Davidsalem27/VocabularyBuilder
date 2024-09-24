import sys
import tkinter as tk

import customtkinter as ctk
import keyboard

import BasicQuizController
import BasicQuizMenu
import WordManager as wm
import MainMenuController
import MainMenu
import time

WAIT_TIME_SECONDS = 300


class MainApp:
    """
    the main program, opens the main menu and a timed quiz according to what the user wants

    """
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    def __init__(self):
        self.root = ctk.CTk()
        self.word_manager = wm.WordManager()
        self.scheduler_on=False
        self.scheduler=None
        self.main_menu_on = False

    def run_main_menu(self):
        self.main_menu_on=True
        print("Running main menu..")
        word_manager=wm.WordManager()
        prog = MainMenuController.MainMenuController(word_manager)
        main_menu=MainMenu.MainMenu(self.root, prog, self.set_quiz_scheduler)
        self.root.mainloop()

    def set_quiz_scheduler(self):
        self.scheduler_on=not self.scheduler_on

    def start_quiz(self):

        word_manager = wm.WordManager()
        controller = BasicQuizController.BasicQuizController(word_manager)
        BasicQuizMenu.BasicQuizMenu(None, controller)


    def run(self):
        self.run_main_menu()
        while True:

            if self.scheduler_on:
                time.sleep(WAIT_TIME_SECONDS)
                self.start_quiz()
            else:
                break
    def on_quiz_close(self, quiz_root):
        quiz_root.destroy()
        print("Quiz closed.")


if __name__ == "__main__":
    main=MainApp()
    main.run()






