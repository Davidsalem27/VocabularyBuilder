from database import WordManager as wm


class QuizMenuController:
    """
     Controller for the quiz menu controller. right now it does nothing, may add functionality
     in future
    """
    def __init__(self, word_manager: wm.WordManager):
        """
        Initializes the QuizMenuController with the specified WordManager.

        :param word_manager: Instance of WordManager for managing words.
        """
        self._word_manager = word_manager


