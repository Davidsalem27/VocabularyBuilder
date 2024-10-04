import random
import WordManager as wm
from Constants import Constants as c


class MultiChoiceQuizController:
    """
    Controller for managing a multiple-choice quiz based on words and their meanings.
    Methods:

        - get_questions(n: int) -> list[tuple[str, list[str], int]]`:
        Generates a list of questions for the quiz.
        - right_answer(word: str) -> None`: Updates the weight of the word upon answering correctly.
    """

    def __init__(self, word_manager: wm.WordManager):
        """
        Initialize the quiz controller.

        :param word_manager: An instance of WordManager to manage words and their meanings.
        """
        self._word_manager = word_manager

    def get_questions(self, n: int) -> list[tuple[str, list[str], int]]:
        """
        Generate a list of questions for the quiz.

        :param n: Number of questions to generate.
        :return: A list of tuples, each containing a word, a list of options, and the index of the correct answer.
        """
        words = self._word_manager.get_n_random_heaviest_words(n)  # List of tuples (word, weight)
        questions = []

        for word in words:
            # Get wrong meanings and put in options
            options = self._word_manager.get_meanings_excluding_word(word)

            # Take the first meaning of the word
            right_meaning = self._word_manager.get_meanings(word)[0][0]

            # Put the right answer in a random place
            right_place = random.randint(0, c.MULTI_CHOICE_NUM_OPTIONS-1)
            options.insert(right_place, right_meaning)

            questions.append((word, options, right_place))

        return questions

    def right_answer(self, word: str) -> None:
        """
        Update the weight of the word upon answering correctly.

        :param word: The word for which the answer was correct.
        """
        self._word_manager.update_weight(word, -1)
