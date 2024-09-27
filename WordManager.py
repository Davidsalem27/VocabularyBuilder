import Database as db
import Word as word
import WordFactory
import Constants as c


class WordManager:
    def __init__(self):
        self.database = db.Database_Manager()
        self.word_factory = WordFactory.WordFactory()

    def add_words_from_textfile(self, path: str = c.FILE_PATH) -> None:
        """
        uses the word_factory to get a list of Word objects and then uses the insert_word
        method from the database class to add the words into the database
        :param path: path of the local file to be loaded
        :return: None
        """
        words=self.word_factory.load_words_local(path)
        for i in range(len(words)):
            self.database.insert_word(words[i])

    def add_word(self, name: str) -> bool:
        new_word = self.word_factory.create_word_web(name)
        self.database.insert_word(new_word)
        return True

    def get_meanings(self, word: str):
        return (self.database.get_meanings_of_word(word))

    def update_weight(self, word: str, weight: int):
        self.database.update_weight(word, weight)

    def close_WordManager(self):
        self.database.close()

    def empty_database(self):
        self.database.clear_tables()

    def delete_word(self, word: str):
        self.database.delete_word(word)

    def get_all_words(self):
        word_tuples = self.database.get_all_words()
        words = []
        for i in range(len(word_tuples)):
            words.append(word_tuples[i][0])
        return words

    def get_all_words_weight(self):
        return self.database.get_all_words()
