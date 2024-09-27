import random
import sqlite3


"""
responsible for communicating with the database that keeps the words
has 3 functionalities - insert a word , delete a word, print the words and their meanings
"""
class Database_Manager:

    def __init__(self,new_database=False):
        self._connection=sqlite3.connect("words.db")
        self._cursor = self._connection.cursor()
        self.create_Table()

    def create_Table(self):
        self._cursor.execute("""
           CREATE TABLE IF NOT EXISTS words (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               word TEXT UNIQUE NOT NULL,
               weight INTEGER NOT NULL
           )
           """)
        # Create meanings table
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
    def delete_word(self,word: str):
        if not self.word_exists(word):
            raise ValueError(word + " doesnt exist in database")
        self._cursor.execute("DELETE FROM words WHERE word = ?", (word,))
        self._connection.commit()
    def update_weight(self,word:str,increment : int):
        self._cursor.execute("UPDATE words SET weight = weight + ? WHERE word = ?"
                             ,(increment, word))
        self._connection.commit()


    def insert_word(self, word):

        if (self.word_exists(word.name)):

            return
        # Insert the word into the words table

        self._cursor.execute("INSERT OR IGNORE INTO words (word, weight) VALUES (?, ?);", (word.name, word.weight))
        self._connection.commit()

        # Get the word ID
        self._cursor.execute("SELECT id FROM words WHERE word = ?;", (word.name,))


        word_id = self._cursor.fetchone()[0]

        # Insert meanings
        for meaning in word.meanings:

            self._cursor.execute(
                "INSERT INTO meanings (word_id, meaning) VALUES (?, ?);",
                (word_id, meaning[0]))
            meaning_id = self._cursor.lastrowid
            if meaning[1]:
                self.insert_example( meaning_id, meaning[1])

        self._connection.commit()

    def insert_example(self, meaning_id, example):
        if example!=0:
            self._cursor.execute("INSERT INTO examples (meaning_id, example) VALUES (?, ?);", (meaning_id, example))
            self._connection.commit()

    def print_all_words(self):
        # self._cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

        words = self.get_all_words()
        if words:
            print("Words in the database:")
            for (word,) in words:  # Unpack the tuple directly
                print(word)
                self.print_meanings_of_word(word)
        else:
            print("No words found in the database.")
    def get_all_words(self):
        self._cursor.execute("SELECT word,weight FROM words;")
        words=self._cursor.fetchall()

        return words

    def fetch_random_weighted_words(self, n, sample_size):
        self._cursor.execute("SELECT * FROM words ORDER BY weight DESC LIMIT ?", (n,))
        top_weighted_words = self._cursor.fetchall()

        # Randomly sample from the top weighted words
        if len(top_weighted_words) <= sample_size:
            random_words = top_weighted_words  # If fewer words than sample size, take all
        else:
            random_words = random.sample(top_weighted_words, sample_size)
        return random_words

    def get_meanings_of_word(self,word_name):
        self._cursor.execute("""
                SELECT meanings.id, meanings.meaning 
                FROM meanings 
                JOIN words ON words.id = meanings.word_id 
                WHERE words.word = ?;
            """, (word_name,))

        meanings = self._cursor.fetchall()
        meanings_to_return=[]

        if meanings:
            for meaning_id, meaning in meanings:  # Unpack the tuple

                # Now query to get examples associated with the current meaning
                self._cursor.execute("""
                                    SELECT example 
                                    FROM examples 
                                    WHERE meaning_id = ?;
                                """, (meaning_id,))

                example = self._cursor.fetchall()

                if example:
                    meanings_to_return.append((meaning,example))
                else:
                    meanings_to_return.append((meaning,None))
            return meanings_to_return
        else:
            print(f"No meanings found for the word '{word_name}'.")

    def print_meanings_of_word(self, word_name):
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

    def word_exists(self, word_name):

        self._cursor.execute("SELECT 1 FROM words WHERE word = ?;", (word_name,))
        if self._cursor.fetchone():
            return True
        return False

    def clear_tables(self):
        # Clear all records from the tables
        self._cursor.execute("DELETE FROM examples;")
        self._cursor.execute("DELETE FROM meanings;")
        self._cursor.execute("DELETE FROM words;")
        self._connection.commit()

    def close(self):
        self._connection.close()





