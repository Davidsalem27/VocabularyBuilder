from main.Constants import Constants as c
from database import Scraper,Word

import re


class WordFactory:
    """
    factory for creating Word object
    """

    def __init__(self):
        self._scraper = Scraper.WebScraper(c.SCRAPER_URL)

    def create_word_web(self, name: str) -> Word.Word:
        """
        crate a new Word with meanings from the scraper
        :param name: the name of the word
        :return: a new Word object
        """
        meanings = self._edit_meanings(self._scraper.read_word(name))
        return Word.Word(name, meanings, c.STARTING_WEIGHT)


    def load_words_local(self, path: str) -> list[Word.Word]:

        """
        function for loading words from local text file and turning them
        into Word objects
        :param path: the path to file
        :return: list of Word objects
        """
        word_names = self._file_reader(path)
        words = []
        for i in range(len(word_names)):
            words.append(self.create_word_web(word_names[i].lower()))
        return words

    def _file_reader(self, path: str) -> list[str]:
        """
        basic function for loading a text file
        :param path: the location of the file
        :return: a list of the words i.e. [word1,word2,...]
        """
        try:
            with open(path, 'r') as file:
                words = [line.strip() for line in file if line.strip()]  # Read and clean lines
            return words
        except FileNotFoundError:
            print(f"Error: The file {path} does not exist.")
            return []

    def _edit_meanings(self, meanings: list[tuple[str, str | int]]) -> list[tuple[str, str | int]]:
        """
        function that returns the meanings list after various editing
        :param meanings: list of meanings and examples [(meaning1,example1)..]
        :return: the edited list
        """
        new_meanings = []
        for i in range(len(meanings)):
            new_meanings.append((self._edit_meaning(meanings[i][0]),
                                 self._edit_example(meanings[i][1])))
        return new_meanings

    def _edit_meaning(self, meaning: str) -> str:
        """
        removes parentheses that have the word sense inside and sense followed
        by an integer
        :param meaning: the meaning to edit
        :return: the edited meaning
        """
        pattern_sense_parent = r'\(.*?\bsense\b.*?\)'
        pattern_sense_dig = r'sense \d+'
        meaning = re.sub(pattern_sense_parent, '', meaning)
        meaning = re.sub(pattern_sense_dig, '', meaning)
        print(meaning)
        return meaning.strip()

    def _edit_example(self, example: str | int) -> str | int:
        """
        remove [] brackets from example, currently doesnt work
        if there is no example then the scraper put a 0 instead
        :param example: the example to work on
        :return: the edited example or 0
        """
        if example ==0:
            return example
        return (re.sub( r'\[.*?\]', '', example)).strip()
