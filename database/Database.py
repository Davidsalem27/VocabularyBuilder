import os
import sqlite3
import sys

from database import Word
from main.Constants import Constants as c


class DatabaseManager:
    """
    Database_Manager provides an interface for managing a SQLite database
    containing words, their meanings, and example sentences.

    Overview:
    The manager handles 3 tables:
    - words: Stores unique words along with their weights.
    - meanings: Stores meanings associated with each word.
    - examples: Stores example sentences linked to each meaning.
    """

    def __init__(self) -> None:
        """
        Initializes the DatabaseManager instance and establishes a connection to the database.
        will create a new database called words if one doesn't already exist

        """
        if hasattr(sys, '_MEIPASS'):
            # Running in a PyInstaller bundle
            self._db_path = os.path.join(sys._MEIPASS, 'assets', 'words.db')
        else:
            # Running in a normal Python environment
            self._db_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'words.db')
        print(f"Connecting to database at: {self._db_path}")
        self._connection = sqlite3.connect(self._db_path)
        self._cursor = self._connection.cursor()
        self._create_Table()

    def _create_Table(self) -> None:
        """
        Creates the necessary tables in the database if they do not already exist.

        This method creates three tables:
        - words: Stores unique words along with their weights.
        - meanings: Stores meanings associated with each word.
        - examples: Stores example sentences related to each meaning.

        :return: None
        """
        self._cursor.execute("""
           CREATE TABLE IF NOT EXISTS words (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               word TEXT UNIQUE NOT NULL,
               weight INTEGER NOT NULL
           )
        """)
        self._cursor.execute("""
           CREATE TABLE IF NOT EXISTS meanings (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               word_id INTEGER,
               meaning TEXT NOT NULL,
               FOREIGN KEY (word_id) REFERENCES words(id) ON DELETE CASCADE
           )
        """)
        self._cursor.execute("""
           CREATE TABLE IF NOT EXISTS examples (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               meaning_id INTEGER,
               example TEXT NOT NULL,
               FOREIGN KEY (meaning_id) REFERENCES meanings(id) ON DELETE CASCADE
           )
        """)
        self._connection.commit()

    def _get_word_id(self, word: str) -> int | None:
        """
        get the word id in the words table of a word
        :param word: the word to look for
        :return: the row id of it
        """
        query = "SELECT id FROM words WHERE word = ?;"
        self._cursor.execute(query, (word,))

        result = self._cursor.fetchone()  # Fetch the result (if any)
        if result:
            return result[0]  # Return the ID if found
        return None

    def get_meanings_excluding_word(self, word: str) -> list[str]:
        print(word)
        self._cursor.execute("SELECT meaning FROM meanings WHERE word_id != ? "
                             "ORDER BY RANDOM() LIMIT 4;",
                             (self._get_word_id(word),))

        meanings = self._cursor.fetchall()  # Fetch all the results
        return [meaning[0] for meaning in meanings]

    def insert_word(self, word: Word.Word) -> None:
        """
        Inserts a new word and its meanings into the database. makes it lowercase
        to avoid bugs

        If the word already exists, it does nothing.

        :param word: A Word object containing the word name, weight, and meanings.
        :return: None
        """
        if self._word_exists(word.name):
            return

        self._cursor.execute(
            "INSERT OR IGNORE INTO words (word, weight) VALUES (?, ?);",
            (word.name, word.weight)
        )
        self._connection.commit()

        self._cursor.execute("SELECT id FROM words WHERE word = ?;", (word.name,))
        word_id = self._cursor.fetchone()[0]

        for meaning in word.meanings:
            self._cursor.execute(
                "INSERT INTO meanings (word_id, meaning) VALUES (?, ?);",
                (word_id, meaning[0])
            )
            meaning_id = self._cursor.lastrowid
            if meaning[1]:
                self.insert_example(meaning_id, meaning[1])

        self._connection.commit()

    def delete_word(self, word: str) -> None:
        """
        Deletes a specified word from the database.

        Raises a ValueError if the word does not exist.

        :param word: The word to be deleted from the database.
        :return: None
        """
        if not self._word_exists(word):
            raise ValueError()
        self._cursor.execute("DELETE FROM words WHERE word = ?", (word,))
        self._connection.commit()

    def update_weight(self, word: str, increment: int) -> None:
        """
        Updates the weight of a specified word by a given increment.

        Raises a ValueError if the word does not exist.

        :param word: The word whose weight is to be updated.
        :param increment: The amount to increment the weight by.
        :return: None
        """
        if not self._word_exists(word):
            raise ValueError()
        self._cursor.execute("UPDATE words SET weight = weight + ? WHERE word = ?", (increment, word))
        self._connection.commit()

    def get_all_words(self) -> list[tuple[str, int]]:
        """
        Retrieves all words and their weights from the database.

        :return: A list of tuples, each containing a word and its weight.
        """
        self._cursor.execute("SELECT word, weight FROM words;")
        return self._cursor.fetchall()



    def get_meanings_of_word(self, word_name: str) -> list[tuple[str, list[str]]]:
        """
        Retrieves meanings and associated examples for a specified word.

        :param word_name: The word for which meanings and examples are to be retrieved.
        :return: A list of tuples, each containing a meaning and its associated examples.
        """
        self._cursor.execute("""
            SELECT meanings.id, meanings.meaning 
            FROM meanings 
            JOIN words ON words.id = meanings.word_id 
            WHERE words.word = ?;
        """, (word_name,))

        meanings = self._cursor.fetchall()
        meanings_to_return = []

        if meanings:
            for meaning_id, meaning in meanings:
                self._cursor.execute("SELECT example FROM examples WHERE meaning_id = ?;", (meaning_id,))
                examples = self._cursor.fetchall()
                meanings_to_return.append((meaning, [example[0] for example in examples] if examples else []))
            return meanings_to_return
        else:
            print(f"No meanings found for the word '{word_name}'.")

    def _word_exists(self, word_name: str) -> bool:
        """
        Checks if a specified word exists in the database by checking the words table.

        :param word_name: The word to check
        :return: True if the word exists, otherwise False.
        """
        self._cursor.execute("SELECT 1 FROM words WHERE word = ?;", (word_name,))
        return bool(self._cursor.fetchone())

    def clear_tables(self) -> None:
        """
        Clears all records from the examples, meanings, and words tables.

        This method permanently deletes all entries in the associated tables
        without any conditions.

        :return: None
        """
        self._cursor.execute("DELETE FROM examples;")
        self._cursor.execute("DELETE FROM meanings;")
        self._cursor.execute("DELETE FROM words;")
        self._connection.commit()

    def insert_example(self, meaning_id: int, example: str) -> None:
        """
        Inserts a new example into the examples table associated with a specific meaning.

        :param meaning_id: The ID of the meaning to which the example belongs.
        :param example: The example text to be inserted.
        :return: None
        """
        if example:
            self._cursor.execute(
                "INSERT INTO examples (meaning_id, example) VALUES (?, ?);",
                (meaning_id, example)
            )
            self._connection.commit()

    def close(self) -> None:
        """
        closes the connection to the database
        :return: None
        """
        self._connection.close()

    ######for testing#######
    def _print_all_words(self):
        # self._cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

        words = self.get_all_words()
        if words:
            print("Words in the database:")
            for (word,) in words:  # Unpack the tuple directly
                print(word)
                self._print_meanings_of_word(word)
        else:
            print("No words found in the database.")

    def _print_meanings_of_word(self, word_name):
        # Query to get meanings associated with the given word
        self._cursor.execute("""
                SELECT meanings.id, meanings.meaning 
                FROM meanings 
                JOIN words ON words.id = meanings.word_id 
                WHERE words.word = ?;
            """, (word_name,))

        meanings = self._cursor.fetchall()

        if meanings:
            print(f"Meanings of the word '{word_name}':")
            for meaning_id, meaning in meanings:  # Unpack the tuple
                print(f"- {meaning}")

                # Now query to get examples associated with the current meaning
                self._cursor.execute("""
                            SELECT example 
                            FROM examples 
                            WHERE meaning_id = ?;
                        """, (meaning_id,))

                examples = self._cursor.fetchall()

                if examples:
                    print("  Examples:")
                    for example, in examples:  # Unpack the tuple
                        print(f"    - {example}")
                else:
                    print("  No examples found.")
        else:
            print(f"No meanings found for the word '{word_name}'.")
