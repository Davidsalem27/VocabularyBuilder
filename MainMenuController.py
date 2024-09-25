
import QuizMenuController
import SettingsLoader
import WordManager as wm
import WordManagerController


class MainMenuController:
    """
    the main menu controller of the model-view-controller design pattern
    """
    def __init__(self,word_manager : wm.WordManager):
        self.word_manager=word_manager


    def open_words_menu(self) -> WordManagerController.WordManagerController:
        return WordManagerController.WordManagerController(self.word_manager)
    def open_quiz_menu(self) -> QuizMenuController.QuizMenuController:
        return QuizMenuController.QuizMenuController(self.word_manager)
    # def open_show_words_menu(self):
    #     return ShowWordsController.ShowWordsController(self.word_manager)
    def open_settings_menu(self):
        settings=SettingsLoader.SettingsEditor().load_file()







