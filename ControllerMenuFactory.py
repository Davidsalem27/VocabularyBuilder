import sys
import threading

from PyQt5.QtWidgets import QApplication, QWidget
import PIL.Image
import pystray
import BasicQuizController
import BasicQuizMenu
import ManageWordsMenu
import QuizMenu
import QuizMenuController
import SetTimedQuizzesController
import SetTimedQuizzesMenu
import SettingsController
import SettingsMenu
import ShowWordsController
import ShowWordsMenu
import WordManager as wm
import MainMenuController
import MainMenu as MainMenu
import ManageWordsController


class ControllerMenuFactory:
    """
    factory for creating couples of controller and menu
    each function creates a couple and returns the gui item i.e. the menu
    sends callbacks to each menu created so they can create a menu on their own
    """
    def __init__(self):
        self.word_manager = wm.WordManager()

    def create_main_menu(self, minimize, close_program) -> MainMenu.MainMenu:
        controller = MainMenuController.MainMenuController(self.word_manager)
        return MainMenu.MainMenu(controller, minimize, close_program,
                                           self.create_manage_words_menu,
                                      self.create_quiz_menu,self.create_settings_menu)
    def create_manage_words_menu(self) -> ManageWordsMenu.ManageWordsMenu:
        manage_words_controller = ManageWordsController.ManageWordsController(self.word_manager)
        return ManageWordsMenu.ManageWordsMenu(manage_words_controller,self.create_show_words_menu)

    def create_quiz_menu(self) -> QuizMenu.QuizMenu:
        quiz_menu_controller = QuizMenuController.QuizMenuController(self.word_manager)
        return QuizMenu.QuizMenu(quiz_menu_controller,self.create_basic_quiz_menu,self.create_timed_quiz_menu)
    def create_basic_quiz_menu(self,num_words_in_quiz=5) -> BasicQuizMenu.BasicQuizMenu:
        basic_quiz_controller = BasicQuizController.BasicQuizController(self.word_manager)
        return BasicQuizMenu.BasicQuizMenu(basic_quiz_controller,num_words_in_quiz)
    def create_settings_menu(self) -> SettingsMenu.SettingsMenu:
        settings_controller = SettingsController.SettingsController(self.word_manager)
        return SettingsMenu.SettingsMenu(settings_controller)
    def create_show_words_menu(self) -> ShowWordsMenu.ShowWordsMenu:
        show_words_controller = ShowWordsController.ShowWordsController(self.word_manager)
        return ShowWordsMenu.ShowWordsMenu(show_words_controller)
    def create_timed_quiz_menu(self):
        controller=SetTimedQuizzesController.SetTimedQuizzesController(self.create_basic_quiz_menu,None)
        return SetTimedQuizzesMenu.SetTimedQuizzesMenu(controller)
