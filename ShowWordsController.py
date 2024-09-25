import WordManager as wm


class ShowWordsController:
    """
    the controller of the model-view-controller design pattern
    """
    def __init__(self,word_manager : wm.WordManager):
        self.word_manager=word_manager

    def get_all_words(self) -> list[str]:
        x= self.word_manager.get_all_words()
        print(x)
        return x
    def get_meaning(self,word) -> list[tuple]:
        return self.word_manager.get_meanings(word)