import MainMenu
import QuizMenuController
import ShowWordsController
import ShowWordsMenu
import WordManager as wm
import MainMenu as gui
import tkinter as tk

import WordManagerController


class MainMenuController:
    """
    the controller of the model-view-controller design pattern
    """
    def __init__(self,word_manager : wm.WordManager):
        self.word_manager=word_manager


    def open_words_menu(self) -> WordManagerController.WordManagerController:
        return WordManagerController.WordManagerController(self.word_manager)
    def open_quiz_menu(self) -> QuizMenuController.QuizMenuController:
        return QuizMenuController.QuizMenuController(self.word_manager)
    # def open_show_words_menu(self):
    #     return ShowWordsController.ShowWordsController(self.word_manager)


    # def delete_word(self, word: str):
    #     self.word_manager.delete_word(word)







