import Database as db

import WordFactory
from Constants import Constants as c


class WordManager:
    """
    Manages the interaction between the word database and the user interface side through controllers.

    The WordManager class provides methods to add, retrieve, update, and delete words in the
    database. It utilizes a DatabaseManager for database operations and a WordFactory to create
    Word objects from various sources (e.g., local files or web sources).

    Attributes:
        _database (DatabaseManager): An instance of DatabaseManager for handling database operations.
        _word_factory (WordFactory): An instance of WordFactory for creating Word objects.

    Methods:
        add_words_from_textfile(path: str) -> None:
            Loads words from a specified text file and adds them to the database.

        add_word(name: str) -> None:
            Adds a single word to the database by creating a Word object.

        get_meanings(word: str) -> list[tuple[str, list[str]]]:
            Retrieves meanings and examples for a specified word.

        update_weight(word: str, weight: int) -> None:
            Updates the weight of a specified word in the database.

        close() -> None:
            Closes the database connection.

        clear_database() -> None:
            Clears all records from the database.

        delete_word(word: str) -> None:
            Deletes a specified word from the database.

        get_all_words() -> list[str]:
            Retrieves all words from the database as a list of strings.

        get_all_words_with_weights() -> list[tuple[str, int]]:
            Retrieves all words and their weights from the database.
    """
    def __init__(self):
        """
        Initializes the WordManager with a database manager and a word factory.
        """
        self._database = db.DatabaseManager()
        self._word_factory = WordFactory.WordFactory()

    def add_words_from_textfile(self, path: str = c.FILE_PATH) -> None:
        """
        Loads words from a text file and adds them to the database.

        Uses the word factory to create Word objects from the file.

        :param path: The path of the local file containing words (default is specified in Constants).
        :return: None
        """
        words = self._word_factory.load_words_local(path)
        for word in words:
            self._database.insert_word(word)

    def add_word(self, name: str) -> None:
        """
        Adds a single word to the database.

        Creates a Word object from a web source and inserts it into the database.

        :param name: The name of the word to be added.
        :return: True if the word is added successfully, False otherwise.
        """
        new_word = self._word_factory.create_word_web(name)
        self._database.insert_word(new_word)


    def get_meanings(self, word: str) -> list[tuple[str, list[str]]]:
        """
        Retrieves meanings and examples for a specified word.

        :param word: The word for which meanings are to be retrieved.
        :return: A list of tuples, each containing a meaning and its associated examples.
        """
        return self._database.get_meanings_of_word(word)

    def update_weight(self, word: str, weight: int) -> None:
        """
        Updates the weight of a specified word.

        :param word: The word whose weight is to be updated.
        :param weight: The new weight to be set for the word.
        :return: None
        """
        self._database.update_weight(word, weight)

    def close_word_manager(self) -> None:
        """
        Closes the database connection.

        :return: None
        """
        self._database.close()

    def empty_database(self) -> None:
        """
        Clears all records from the database.

        :return: None
        """
        self._database.clear_tables()

    def delete_word(self, word: str) -> None:
        """
        Deletes a specified word from the database.

        :param word: The word to be deleted.
        :return: None
        """
        self._database.delete_word(word)

    def get_all_words(self) -> list[str]:
        """
        Retrieves all words from the database.

        :return: A list of all words in str (not Word object).
        """
        word_tuples = self._database.get_all_words()
        return [word_tuple[0] for word_tuple in word_tuples]

    def get_all_words_weight(self) -> list[tuple[str, int]]:
        """
        Retrieves all words and their weights from the database.

        :return: A list of tuples, each containing a word and its weight.
        """
        return self._database.get_all_words()
