from PyQt5.QtWidgets import QApplication, QWidget

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
from Constants import Constants as c

class ControllerMenuFactory:
    """
    Factory for creating pairs of controller and menu.
    Each function creates a couple and returns the GUI item with corresponding controller
    saved into a field.

    Fields:
        word_manager (WordManager): Instance of the WordManager for managing words.
    """

    def __init__(self) -> None:
        """Initializes the factory with a WordManager instance.

        :return: None
        """
        self.word_manager = wm.WordManager()

    def create_main_menu(self, minimize: callable, close_program: callable) -> MainMenu.MainMenu:
        """Creates the main menu with associated controller and callbacks.

        :param minimize: Function to minimize the main window.
        :param close_program: Function to close the application.
        :return: The created main menu.
        """
        controller = MainMenuController.MainMenuController(self.word_manager)
        return MainMenu.MainMenu(controller, minimize, close_program,
                                 self.create_manage_words_menu,
                                 self.create_quiz_menu,
                                 self.create_settings_menu)

    def create_manage_words_menu(self) -> ManageWordsMenu.ManageWordsMenu:
        """Creates the manage words menu with its controller.

        :return: The created manage words menu.
        """

        manage_words_controller = ManageWordsController.ManageWordsController(self.word_manager)
        return ManageWordsMenu.ManageWordsMenu(manage_words_controller, self.create_show_words_menu)

    def create_quiz_menu(self) -> QuizMenu.QuizMenu:
        """Creates the quiz menu with its controller.

        :return: The created quiz menu.
        """
        quiz_menu_controller = QuizMenuController.QuizMenuController(self.word_manager)
        return QuizMenu.QuizMenu(quiz_menu_controller, self.create_basic_quiz_menu, self.create_timed_quiz_menu)

    def create_basic_quiz_menu(self, num_words_in_quiz=c.DEFAULT_NUM_WORDS) -> BasicQuizMenu.BasicQuizMenu:
        """Creates the basic quiz menu with its controller.

        :param num_words_in_quiz: Number of words to include in the quiz.
        default is 5
        :return: The created basic quiz menu.
        """
        basic_quiz_controller = BasicQuizController.BasicQuizController(self.word_manager)
        return BasicQuizMenu.BasicQuizMenu(basic_quiz_controller, num_words_in_quiz)

    def create_settings_menu(self) -> SettingsMenu.SettingsMenu:
        """Creates the settings menu with its controller.

        :return: The created settings menu.
        """
        settings_controller = SettingsController.SettingsController(self.word_manager)
        return SettingsMenu.SettingsMenu(settings_controller)

    def create_show_words_menu(self) -> ShowWordsMenu.ShowWordsMenu:
        """Creates the show words menu with its controller.

        :return: The created show words menu.
        """
        show_words_controller = ShowWordsController.ShowWordsController(self.word_manager)
        return ShowWordsMenu.ShowWordsMenu(show_words_controller)

    def create_timed_quiz_menu(self) -> SetTimedQuizzesMenu.SetTimedQuizzesMenu:
        """Creates the timed quiz menu with its controller.

        :return: The created timed quiz menu.
        """
        controller = SetTimedQuizzesController.SetTimedQuizzesController(self.create_basic_quiz_menu, None)
        return SetTimedQuizzesMenu.SetTimedQuizzesMenu(controller)
