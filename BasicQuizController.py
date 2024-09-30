import WordManager as wm
import random
from typing import List, Tuple


class BasicQuizController:
    """
    Controller for managing the basic quiz.

    This class interacts with a WordManager instance to retrieve words,
    their definitions, and manage their difficulty ratings.

    Methods:
        get_n_definitions(n: int) -> List[Tuple[str, List[Tuple[str, List[str]]]]:
            Retrieves n random definitions based on word weights.

        update_word_easy(word: str) -> None:
            Updates the weight of a word to make it easier.

        update_word_hard(word: str) -> None:
            Updates the weight of a word to make it harder.
    """

    def __init__(self, word_manager: wm.WordManager):
        """
        Initializes the BasicQuizController with a WordManager instance.

        :param word_manager: An instance of WordManager to manage words and their meanings.
        """
        self._word_manager = word_manager

    def get_n_definitions(self, n: int) -> list[tuple[str, list[tuple[str, list[str]]]]]:
        """
        Retrieves n random definitions based on the weights of words.

        The words are sorted by their weights, and n random words are chosen
        from the highest-weighted words. Their definitions are then fetched.

        :param n: The number of definitions to retrieve.
        :return: A list of tuples where each tuple contains a word and its corresponding definitions.
        """
        words = self._word_manager.get_all_words_weight()
        sorted_words_weights = sorted(words, key=lambda x: x[1], reverse=True)
        randomized_lst = self._get_n_random_words_weight(n, sorted_words_weights)

        definitions = []
        for word in randomized_lst:
            definitions.append((word, self._word_manager.get_meanings(word)))

        return definitions

    def _get_n_random_words_weight(self, n: int, sorted_words_weights: list[tuple[str, int]]) -> List[str]:
        """
        Selects n random words from the sorted list of words based on their weights.

        The method ensures that words of the same weight are handled together to maintain randomness.

        :param n: The number of random words to select.
        :param sorted_words_weights: A list of tuples containing words and their weights, sorted by weight.
        :return: A list of n randomly selected words.
        """
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
                    tmp_lst.append(sorted_words_weights[i + j][0])
                else:
                    break

            sample_size = min(n - len(randomized_lst), len(tmp_lst))
            randomized_lst += random.sample(tmp_lst, sample_size)
            tmp_lst.clear()

        return randomized_lst

    def update_word_easy(self, word: str) -> None:
        """
        Updates the difficulty weight of a word to make it easier.

        This method decreases the weight of the specified word, indicating
        that it should be considered easier in future quizzes.

        :param word: The word to be updated.
        """
        self._word_manager.update_weight(word, -1)

    def update_word_hard(self, word: str) -> None:
        """
        Updates the difficulty weight of a word to make it harder.

        This method increases the weight of the specified word, indicating
        that it should be considered harder in future quizzes.

        :param word: The word to be updated.
        """
        self._word_manager.update_weight(word, 1)
