from typing import Union, Tuple, List

from bs4 import BeautifulSoup
import requests
import re


class WebScraper:

    def __init__(self , website_used : str="https://www.merriam-webster.com/dictionary/"):
        self.website_used=website_used

    def add_word(self , name_word: str)  -> List[Tuple[str, Union[str, int]]]:# [(),(),()..]
        url=self.website_used+name_word
        result = requests.get(url)
        doc_web = BeautifulSoup(result.text,"html.parser")
        definition = doc_web.find('div', class_='vg')
        meanings = definition.find_all('div', class_='vg-sseq-entry-item')
        list_meanings=[]
        for meaning in meanings:

            submeanings = meaning.find_all('span', class_="dt")  # the smallest definition
            for submeaning in submeanings:
                mean = submeaning.find('span', class_="dtText")
                example_sent = submeaning.find('div', class_="sub-content-thread")
                # rv[1]+=[mean.get_text()]
                print(mean.get_text())
                if example_sent:
                    # rv[1] += [example_sent.get_text()]
                    list_meanings.append((mean.get_text(),example_sent.get_text()))
                    print(example_sent.get_text())
                else:
                    list_meanings.append((mean.get_text(),0))
        return list_meanings


