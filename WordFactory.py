import Word as word
import Scraper as scraper
from Constants import Constants as c

class WordFactory:
    """
    factory for creating Word object
    """
    def __init__(self):
        self._scraper=scraper.WebScraper()

    def create_word_web(self, name: str) -> word.Word:
        """
        crate a new Word with meanings from the scraper
        :param name: the name of the word
        :return: a new Word object
        """
        meanings=self._scraper.read_word(name)
        new_word=word.Word(name,meanings,c.STARTING_WEIGHT)
        return new_word

    def load_words_local(self, path: str) -> list[word.Word]:

        """
        function for loading words from local text file and turning them
        into Word objects
        :param path: the path to file
        :return: list of Word objects
        """
        word_names=self._file_reader(path)
        words=[]
        for i in range(len(word_names)):
            words.append(self.create_word_web(word_names[i]))
        return words
    def _file_reader(self,path : str) -> list[str]:
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
