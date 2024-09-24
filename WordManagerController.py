import ShowWordsController
import WordManager as wm

class WordManagerController:
    """
    the controller of the model-view-controller design pattern
    """
    def __init__(self,word_manager : wm.WordManager):
        self.word_manager=word_manager

    def get_meanings(self,word: str)-> bool:
        self.word_manager.get_meanings(word)
        return True

    def submit_new_word(self, new_word: str) -> bool:
         # Get the user input from the GUI entry
        if self.word_manager.add_word(new_word):
            return True
        return False

    def get_all_words(self) ->list[str]:
        return self.word_manager.get_all_words()

    def delete_word(self, word: str):
        self.word_manager.delete_word(word)
    def open_show_words_menu(self):
        return ShowWordsController.ShowWordsController(self.word_manager)