import BasicQuizController
import WordManager as wm
class QuizController:

    def __init__(self, word_manager: wm.WordManager):
        self.word_manager = word_manager

    def open_basic_quiz(self):
        return BasicQuizController.BasicQuizController(self.word_manager)

