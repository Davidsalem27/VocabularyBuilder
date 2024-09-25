import Database as db
import Word as word
import WordFactory

FILE_PATH="ListWords.txt"
class WordManager:
    def __init__(self):
        self.database=db.Database_Manager()
        self.word_factory = WordFactory.WordFactory()


    def add_words_from_textfile(self, path=FILE_PATH) ->bool:
        words=[]
        try:
            with open(path, 'r') as file:
                words = [line.strip() for line in file if line.strip()]  # Read and clean lines
        except FileNotFoundError:
            print(f"Error: The file {path} does not exist.")
            return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
        for i in range(len(words)):
            self.add_word(words[i])
        return True
    def add_word(self,name : str) -> bool:
        if (name==""):
            return
        try:
            new_word=self.word_factory.create_word_web(name)
        except Exception:
            print("problem with word")
            return
        self.database.insert_word(new_word)
        return True
    def get_meanings(self,word:str):
        return (self.database.get_meanings_of_word(word))

    def update_weight(self,word:str,weight : int):
        self.database.update_weight(word,weight)
    def close_WordManager(self):
        self.database.close()
    def empty_database(self):
        self.database.clear_tables()
    def delete_word(self,word : str):
        self.database.delete_word(word)
    def get_all_words(self):

        word_tuples=self.database.get_all_words()
        words=[]
        for i in range(len(word_tuples)):
            words.append(word_tuples[i][0])
        return words
    def get_all_words_weight(self):

        return self.database.get_all_words()



















