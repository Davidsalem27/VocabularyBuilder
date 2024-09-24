import Word as word
import Scraper as scraper

class WordFactory:
    """
    factory for creating Word object
    """
    def __init__(self):
        self.scraper=scraper.WebScraper()

    def create_word_web(self, name: str) -> word.Word:
        """
        crate a new Word, uses mirriam webster
        :param name: the name of the word
        :return: a new Word object
        """
        meanings=self.scraper.add_word(name) #add test return [[str][list of tuples]]
        new_word=word.Word(name,meanings,1)
        return new_word

    def load_words_local(self, path: str) -> word.Word:
        """load from a local file"""
        pass