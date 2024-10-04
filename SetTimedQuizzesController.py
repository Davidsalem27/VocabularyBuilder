from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMessageBox

from Constants import Constants as c

class SetTimedQuizzesController:
    """
    controller for the timed quizzes, once open_quiz is called by the SetTimedQuizzesMenu
    the controller uses functions from the MenuControllerfactory and a timer to create the
    quizzes according to what the user chose

     Methods
    -------
    open_quiz(self, time_interval : str, num_words: str, quiz_type: str) -> None:
        starts the timer with the parameters the user chose in the menu
    """
    def __init__(self, create_basic_quiz, create_multichoice_quiz):

        self._num_words = None
        self._create_basic_quiz=create_basic_quiz
        self._create_multi_choice_quiz=create_multichoice_quiz
        self._timer = QTimer()
        self._quiz_type=None
        self._timer.timeout.connect(self._create_quiz)
        self._active = True



    def open_quiz(self, time_interval : str, num_words: str, quiz_type: str) -> None:
        """
        function for making a timed quiz, called by SetTimedQuizzesMenu
        and starts the timer that calles the creating function after the time interval
        :param time_interval: the time interval between each quiz, is multiplied by HOUR_TO_MILLISECOND
        because setInterval works in miliseconds
        :param num_words: num of words for the timed quiz
        :param quiz_type: the type of quiz to open after the interval
        :return:
        """
        try:
            self._check_parameters(time_interval,num_words)
            self._quiz_type=quiz_type
            self._num_words=int(num_words)
            self._timer.setInterval(int(time_interval)*c.HOUR_TO_MILLISECOND)
            self._timer.start()
        except ValueError as ve:
            self._show_error_message(str(ve))




    def _create_quiz(self) -> None:
        """
        similar to a switch statement, calls a function in the factory class to create
        the type of quiz the user chose, the function is received via callback
        :return:
        """
        if self._quiz_type=="Basic Quiz":
            self._create_basic_quiz(self._num_words)
        if self._quiz_type=="Multiple Choice Quiz":
            self._create_multi_choice_quiz(self._num_words)

    def _show_error_message(self, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Error")
        msg_box.setText(f"An error occurred: {message}")
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()

    def _check_parameters(self, time_interval : str, num_words: str):
        if int(time_interval)<1 or int(time_interval)>24:
            raise ValueError("time interval has to be between 1 and 24 hours")
        if int(num_words)<1 or int(num_words)>50:
            raise ValueError("number of words has to be between 1 and 50")

