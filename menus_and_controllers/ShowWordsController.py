from database import WordManager as wm


class ShowWordsController:
    """
    Controller for managing word retrieval and meanings.

    Fields:
        _word_manager (wm.WordManager): Instance of the WordManager responsible for
                                          handling word data.
    Methods:
        get_all_words() -> list[str]:
            Retrieves all words from the word manager.

        get_meaning(word: str) -> list[tuple]:
            Retrieves the meanings of a specified word.
    """

    def __init__(self, word_manager: wm.WordManager) -> None:
        """
        Initializes the ShowWordsController with a WordManager instance.

        :param word_manager: An instance of WordManager for managing words.
        """
        self._word_manager = word_manager

    def get_all_words(self) -> list[str]:
        """
        Retrieves all words from that are in the database.

        :return: A list of all words.
        """
        return self._word_manager.get_all_words()

    def get_meaning(self, word: str) -> list[tuple]:
        """
        Retrieves the meanings of a specific word in the database.

        :param word: The word whose meanings are to be retrieved.
        :return: A list of tuples containing meanings of the word.
        """
        return self._word_manager.get_meanings(word)
