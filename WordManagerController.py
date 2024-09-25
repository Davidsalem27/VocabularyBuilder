import ShowWordsController
import WordManager as wm
import Exceptions


class WordManagerController:
    """
    the controller of the model-view-controller design pattern
    """
    def __init__(self,word_manager : wm.WordManager):
        self.word_manager=word_manager
    def load_local_file(self):
        self.word_manager.add_words_from_textfile()
    def delete_all_words(self):
        self.word_manager.empty_database()
    def get_meanings(self,word: str)-> bool:
        self.word_manager.get_meanings(word)
        return True

    def add_new_word(self, new_word: str) -> str:
         # Get the user input from the GUI entry
        try:
            self.word_manager.add_word(new_word)
            return (f'Word added to database: {new_word}')
        except Exceptions.URLException:
            return ("problem with adding " + new_word +", please check spelling" )
        except ValueError:
            return ("Please write word before trying to add")

    def get_all_words(self) ->list[str]:
        return self.word_manager.get_all_words()

    def delete_word(self, word: str):
        self.word_manager.delete_word(word)
    def open_show_words_menu(self):
        return ShowWordsController.ShowWordsController(self.word_manager)