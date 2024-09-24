import WordManager as wm

class BasicQuizController:

    def __init__(self, word_manager: wm.WordManager):
        self.word_manager = word_manager


    def get_n_definitions(self,n=5):
        words=self.word_manager.get_all_words_weight()
        print(words)
        sorted_words_weights = sorted(words, key=lambda x: x[1],reverse=True)
        print(sorted_words_weights )
        definitions=[]
        for i in range(n):
            next_word=sorted_words_weights[i][0]
            definitions.append((next_word,self.word_manager.get_meanings(next_word)))
        return definitions
    def update_word_easy(self,word):
        self.word_manager.update_weight(word,-1)
    def update_word_hard(self,word):
        self.word_manager.update_weight(word,1)