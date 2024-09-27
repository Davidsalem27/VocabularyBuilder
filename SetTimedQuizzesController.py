from PyQt5.QtCore import QTimer


import Constants as c

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
    def __init__(self,create_basic_quiz,create_basic_quiz2):

        self._num_words = None
        self._create_basic_quiz=create_basic_quiz
        self._create_basic_quiz2=create_basic_quiz2
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
        self._quiz_type=quiz_type
        self._num_words=int(num_words)
        self._timer.setInterval(int(time_interval)*c.HOUR_TO_MILLISECOND)
        self._timer.start()

    def _create_quiz(self) -> None:
        """
        similar to a switch statement, calls a function in the factory class to create
        the type of quiz the user chose, the function is received via callback
        :return:
        """
        if self._quiz_type=="Basic Quiz":
            self._create_basic_quiz(self._num_words)
        if self._quiz_type=="Basic Quiz 2":
            self._create_basic_quiz2(self._num_words)

