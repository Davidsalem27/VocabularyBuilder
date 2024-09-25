import Word as word
import Scraper as scraper

STARTING_WEIGHT=10
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
        new_word=word.Word(name,meanings,STARTING_WEIGHT)
        return new_word

    def load_words_local(self, path: str) -> word.Word:
        """load from a local file"""
        try:
            with open(path, 'r') as file:
                words = [line.strip() for line in file if line.strip()]  # Read and clean lines
            return words
        except FileNotFoundError:
            print(f"Error: The file {path} does not exist.")
            return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
