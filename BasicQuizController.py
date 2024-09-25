import WordManager as wm
import random


class BasicQuizController:

    def __init__(self, word_manager: wm.WordManager):
        self.word_manager = word_manager

    def get_n_definitions(self, n):
        words = self.word_manager.get_all_words_weight()
        sorted_words_weights = sorted(words, key=lambda x: x[1], reverse=True)
        print(sorted_words_weights)
        weighted_words=[]
        length_weighted_words=0
        curr_weight=sorted_words_weights[0][1] #get maximum weight
        j=0
        while length_weighted_words<n:
            print("1")
            curr_weight = sorted_words_weights[j][1]#take the current biggest weight
            temp_lst=[]
            while curr_weight==sorted_words_weights[j][1] and len(temp_lst)<n:#while we still have words with same weight
                print("2")
                print(sorted_words_weights[j][0])
                temp_lst.append(sorted_words_weights[j][0])
                j+=1
            if len(temp_lst)>0: #if true then we found words
                print("5")
                # random_words=random.choices(temp_lst, k=len(temp_lst))
                # weighted_words.append(random_words[:(n - length_weighted_words)])
                if len(temp_lst)>n-length_weighted_words:
                    print("3")
                    size_to_take=n-length_weighted_words
                    tmp=random.sample(temp_lst, size_to_take)
                    weighted_words+=tmp [:size_to_take]
                    length_weighted_words += size_to_take
                else:
                    print("4")
                    weighted_words+=temp_lst
                    length_weighted_words += len(temp_lst)
                temp_lst.clear()
        print(weighted_words)
        definitions = []
        for i in range(len(weighted_words)):
            next_word=weighted_words[i]
            definitions.append((next_word,self.word_manager.get_meanings(next_word)))
        return definitions

    def update_word_easy(self, word):
        self.word_manager.update_weight(word, -1)

    def update_word_hard(self, word):
        self.word_manager.update_weight(word, 1)
