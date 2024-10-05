from PyQt5.QtWidgets import QMessageBox

from database import WordManager as wm
from main import Exceptions


class ManageWordsController:
    """
    Controller for the managing words menu.

    Fields:
        _word_manager (wm.WordManager): Instance of WordManager for communicating
         with the database.

    Methods:
        load_local_file() -> str:
            Loads words from a local text file into the word manager.

        delete_all_words() -> None:
            Deletes all words from the database.

        add_new_word(new_word: str) -> str:
            Adds a new word to the database.

        get_all_words() -> list[str]:
            Retrieves all words from the word manager.

        delete_word(word: str) -> str:
            Deletes a specific word from the database.
    """

    def __init__(self, word_manager: wm.WordManager) -> None:
        """
        Initializes the ManageWordsController with a WordManager instance.

        :param word_manager: An instance of WordManager to manage word operations.
        """
        self._word_manager = word_manager

    def load_local_file(self) -> str:
        """
        Loads words from a local text file into the word manager.
        if an exception occurs a msg is returned
        :return: A message indicating the result of the load operation.
        """
        try:
            self._word_manager.add_words_from_textfile()
        except Exceptions.URLException as e:
            self._show_error_message("Problem with the word " + str(e) + ", maybe spelling is wrong?")
        else:
            return "Text file loaded successfully"

    def delete_all_words(self) -> None:
        """
        Deletes all words from the database.
        """
        self._word_manager.empty_database()

    def add_new_word(self, new_word: str) -> str:
        """
        Adds a new word to the database.

        :param new_word: The word to be added.
        :return: A message indicating the result of the add operation.
        """
        try:
            self._word_manager.add_word(new_word)
            return f'Word added to database: {new_word}'
        except Exceptions.URLException:
            self._show_error_message("Problem with adding " + new_word + ", please check spelling.")
        except ValueError:
            self._show_error_message("Please write a word before trying to add.")

    def get_all_words(self) -> list[str]:
        """
        Retrieves all words from the word manager.

        :return: A list of all words in the database.
        """
        return self._word_manager.get_all_words()

    def delete_word(self, word: str) -> str:
        """
        Deletes a specific word from the database.

        :param word: The word to be deleted.
        :return: A message indicating the result of the delete operation.
        """
        try:
            self._word_manager.delete_word(word)
            return word + " deleted successfully"
        except ValueError:
            self._show_error_message(word + " Not in Database")

    def _show_error_message(self, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Error")
        msg_box.setText(f"An error occurred: {message}")
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()

