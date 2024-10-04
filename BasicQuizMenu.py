from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QHBoxLayout, QPushButton, QLabel


import BasicQuizController
from Constants import Constants as c

class BasicQuizMenu(QWidget):
    """
    A GUI for managing a basic quiz interface to display words and their definitions.

    This class creates a window and when the next or prev buttons are pressed a new one
    is created. users can reveal meanings and rate the difficulty of the words.
    every meaning can be revealed once per quiz
    """

    def __init__(self, controller: BasicQuizController.BasicQuizController, num_words: int):
        """
        Initializes the BasicQuizMenu with a controller and the number of words.

        :param controller: The controller managing quiz logic and word definitions.
        :param num_words: The number of words to be displayed in the quiz.
        """
        super().__init__()
        self._num_words = num_words
        self._controller = controller
        self._current_window_index = 0
        self.meanings_revealed=[False]*num_words
        self._current_word = ""
        self._current_meaning = None
        self._definitions = self._controller.get_n_definitions(self._num_words)
        self._initUI()

    def _initUI(self) -> None:
        """
        Initializes the user interface components.
        """
        self.setWindowTitle("Basic Quiz")
        self.setGeometry(c.BASIC_QUIZ_MENU_POSX, c.BASIC_QUIZ_MENU_POSY,
                         c.BASIC_QUIZ_MENU_WIDTH, c.BASIC_QUIZ_MENU_HEIGHT)

        self._layout = QVBoxLayout(self)
        # Create a scroll area for meanings and examples
        self._scroll_area = QScrollArea(self)
        self._scroll_area.setWidgetResizable(True)
        self._scroll_content = QWidget()  # Create a content widget for the scroll area
        self._scroll_layout = QVBoxLayout(self._scroll_content)

        self._layout.addWidget(self._scroll_area)
        self._scroll_area.setWidget(self._scroll_content)

        # Create navigation buttons
        button_layout = QHBoxLayout()

        self._prev_button = QPushButton("Previous", self)
        self._prev_button.clicked.connect(self._prev_window)
        self._prev_button.setFixedSize(c.BASIC_QUIZ_MENU_BUTTON_WIDTH,
                                       c.BASIC_QUIZ_MENU_BUTTON_HEIGHT)
        button_layout.addWidget(self._prev_button)

        self._next_button = QPushButton("Next", self)
        self._next_button.clicked.connect(self._next_window)
        self._next_button.setFixedSize(c.BASIC_QUIZ_MENU_BUTTON_WIDTH,
                                       c.BASIC_QUIZ_MENU_BUTTON_HEIGHT)
        button_layout.addWidget(self._next_button)

        self._reveal_button = QPushButton("Reveal meaning!", self)
        self._reveal_button.clicked.connect(self._reveal_check)
        self._reveal_button.setFixedSize(c.BASIC_QUIZ_MENU_BUTTON_WIDTH,
                                       c.BASIC_QUIZ_MENU_BUTTON_HEIGHT)
        button_layout.addWidget(self._reveal_button)

        self._easy_button = QPushButton("Easy", self)
        self._easy_button.clicked.connect(lambda: self._easy_word(self._current_word))
        self._easy_button.setFixedSize(c.BASIC_QUIZ_MENU_BUTTON_WIDTH,
                                       c.BASIC_QUIZ_MENU_BUTTON_HEIGHT)
        button_layout.addWidget(self._easy_button)

        self._mid_button = QPushButton("almost got it", self)
        self._mid_button.clicked.connect(lambda: self._mid_word(self._current_word))
        self._mid_button.setFixedSize(c.BASIC_QUIZ_MENU_BUTTON_WIDTH,
                                       c.BASIC_QUIZ_MENU_BUTTON_HEIGHT)
        button_layout.addWidget(self._mid_button)

        self._hard_button = QPushButton("no idea", self)
        self._hard_button.clicked.connect(lambda: self._hard_word(self._current_word))
        self._hard_button.setFixedSize(c.BASIC_QUIZ_MENU_BUTTON_WIDTH,
                                       c.BASIC_QUIZ_MENU_BUTTON_HEIGHT)
        button_layout.addWidget(self._hard_button)

        self._layout.addLayout(button_layout)

        self._create_window()
        self.show()

    def _create_window(self) -> None:
        """
        Creates and displays the current word and its layout in the UI.
        every meaning can be revealed once
        """
        self._clear_ui()
        word_label = QLabel("", self)
        self._current_word = self._definitions[self._current_window_index][0]
        word_label.setText(self._current_word)

        word_label.setStyleSheet(c.BASIC_QUIZ_WORD_LABEL_STYLE)
        self._scroll_layout.addWidget(word_label, alignment=Qt.AlignCenter)
        if self.meanings_revealed[self._current_window_index]:
            self._reveal_meaning()
    def _clear_ui(self):
        for i in reversed(range(self._scroll_layout.count())):
            widget = self._scroll_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
    def _reveal_check(self) -> None:
        """
        checks if the meaning was already revealed to avoid duplicate
        """
        if self.meanings_revealed[self._current_window_index]:
            pass
        else:
            self._reveal_meaning()
    def _reveal_meaning(self) -> None:
        """
        shows the meanings and examples of the current word on screen after the user
        clicks the reveal meanings button
        """
        self.meanings_revealed[self._current_window_index]=True
        current_meaning = self._definitions[self._current_window_index][1]

        for index, (meaning, example) in enumerate(current_meaning):
            meaning_label = QLabel(f"{index + 1}. {meaning}", self)
            meaning_label.setWordWrap(True)
            meaning_label.setStyleSheet(c.BASIC_QUIZ_MEANING_EXAMPLE_LABEL_STYLE)
            self._scroll_layout.addWidget(meaning_label)

            if example:
                example_label = QLabel(f"   Example: {example}", self)
                example_label.setWordWrap(True)
                example_label.setStyleSheet(c.BASIC_QUIZ_MEANING_EXAMPLE_LABEL_STYLE)
                self._scroll_layout.addWidget(example_label)

    def _easy_word(self, word: str) -> None:
        """
        Updates the difficulty weight of a word to make it easier.

        :param word: The word to be rated as easy.
        """
        self._controller.update_word_easy(word)
    def _mid_word(self, word: str) -> None:
        """
        Updates the difficulty weight of a word to make it easier.

        :param word: The word to be rated as easy.
        """
        self._controller.update_word_mid(word)

    def _hard_word(self, word: str) -> None:
        """
        Updates the difficulty weight of a word to make it harder.

        :param word: The word to be rated as hard.
        """
        self._controller.update_word_hard(word)

    def _next_window(self) -> None:
        """
        Moves to the next word in the quiz if available.
        """
        if self._current_window_index < len(self._definitions) - 1:
            self._current_window_index += 1
            self._create_window()

    def _prev_window(self) -> None:
        """
        Moves to the previous word in the quiz if available.
        """
        if self._current_window_index > 0:
            self._current_window_index -= 1
            self._create_window()
