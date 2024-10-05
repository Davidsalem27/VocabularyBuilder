from typing import Union
from bs4 import BeautifulSoup
import requests
from main.Exceptions import URLException


class WebScraper:
    """
    A class for scraping definitions from the Merriam-Webster dictionary.
    could use any other dictionary as long as its url is "website/word"
    Methods
    -------
    add_word(self, name_word: str) -> List[Tuple[str, Union[str, int]]]:
    function that gets the meanings of a word and examples if there are any and
    return a list of tuples of meaning,example
    """

    def __init__(self, website_used: str):
        """
        Initializes the WebScraper with the specified website.
        :param website_used: The URL of the dictionary website.
        """
        self._website_used = website_used

    def read_word(self, name_word: str) -> list[tuple[str, Union[str, int]]]:
        """
        Retrieves the meanings of the specified word from the dictionary website.

        :param name_word: The word to look up in the dictionary.
        :raises ValueError: If the provided word is an empty string.
        :raises URLException: If the word is not found on the dictionary website.
        :return: A list of tuples, where each tuple contains the meaning and an example sentence
                 or 0 if no example is found. Format: [(meaning1, example1), (meaning2, example2), ...]
        """
        if name_word == "":
            raise ValueError("empty string is not a word")

        url = self._website_used + name_word
        result = requests.get(url)

        doc_web = BeautifulSoup(result.text, "html.parser")

        definition = doc_web.find('div', class_='vg')

        if not definition:
            raise URLException(name_word)

        meanings = definition.find_all('div', class_='vg-sseq-entry-item')

        list_meanings = []
        for meaning in meanings:
            submeanings = meaning.find_all('span', class_="dt")  # the smallest definition
            for submeaning in submeanings:
                mean = submeaning.find('span', class_="dtText")
                example_sent = submeaning.find('div', class_="sub-content-thread")

                if example_sent:
                    list_meanings.append((mean.get_text(), example_sent.get_text()))
                else:
                    list_meanings.append((mean.get_text(), 0))

        return list_meanings
