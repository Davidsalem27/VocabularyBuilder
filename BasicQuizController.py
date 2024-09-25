import WordManager as wm
import random


class BasicQuizController:

    def __init__(self, word_manager: wm.WordManager):
        self.word_manager = word_manager

    def get_n_definitions(self, n):
        words = self.word_manager.get_all_words_weight()
        sorted_words_weights = sorted(words, key=lambda x: x[1], reverse=True)
        weighted_words = []
        randomized_lst=self.get_n_random_words_weight(n,sorted_words_weights)
        definitions = []
        for i in range(len(randomized_lst)):
            next_word = randomized_lst[i]
            definitions.append((next_word, self.word_manager.get_meanings(next_word)))

        return definitions
    def get_n_random_words_weight(self,n,sorted_words_weights):
        max_weight = 0
        tmp_lst = []

        randomized_lst = []
        for i in range(len(sorted_words_weights)):
            if len(randomized_lst) == n:
                break
            if max_weight == sorted_words_weights[i][1]:
                continue
            max_weight = sorted_words_weights[i][1]
            for j in range(len(sorted_words_weights) - i):
                if sorted_words_weights[i + j][1] == max_weight:
                    print(sorted_words_weights[i + j])
                    print(sorted_words_weights[i + j][0])
                    tmp_lst.append(sorted_words_weights[i + j][0])
                else:
                    break
            print(tmp_lst)
            sample_size = min(n - len(randomized_lst), len(tmp_lst))
            randomized_lst += random.sample(tmp_lst, sample_size)

            tmp_lst.clear()
        return randomized_lst
    def update_word_easy(self, word):
        self.word_manager.update_weight(word, -1)

    def update_word_hard(self, word):
        self.word_manager.update_weight(word, 1)
