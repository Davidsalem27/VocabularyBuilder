from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QLineEdit, QPushButton, QLabel
from Constants import Constants as c


class SetTimedQuizzesMenu(QWidget):
    """
    Menu for setting timed quizzes.

    This widget allows users to select a quiz type, set a time interval
    between quizzes, and specify the number of words per quiz. It also
    provides buttons to set the quiz and go back to the previous menu.
    """

    def __init__(self, controller: object) -> None:
        """
        Initializes the SetTimedQuizzesMenu.

        :param controller: An instance of the controller that manages the timer and creation
        of the timed quiz.
        """
        super().__init__()
        self._controller = controller
        self.setWindowTitle("Set a Quiz")
        self.setGeometry(c.SET_TIMED_QUIZ_MENU_POSX, c.SET_TIMED_QUIZ_MENU_POSY,
                         c.SET_TIMED_QUIZ_MENU_WIDTH, c.SET_TIMED_QUIZ_MENU_HEIGHT)
        self._init_ui()

    def _init_ui(self) -> None:
        """Initializes the UI components for the timed quizzes menu."""
        # Set up the main layout
        self._layout = QVBoxLayout(self)

        # Dropdown menu
        self._quiz_type = QComboBox()
        self._quiz_type.addItems(["Basic Quiz", "Multiple Choice Quiz"])
        self._quiz_type.setFont(c.SET_TIMED_QUIZ_FONT)
        self._label_select=QLabel("Select a Quiz:")
        self._label_select.setFont(c.SET_TIMED_QUIZ_FONT)
        self._layout.addWidget(self._label_select)

        self._layout.addWidget(self._quiz_type)

        # Entry fields with labels
        self._label1 = QLabel("Set the time interval between quizzes in hours:")
        self._label1.setFont(c.SET_TIMED_QUIZ_FONT)
        self._entry_time_interval = QLineEdit("3")

        self._entry_time_interval.setFixedSize(c.SET_TIMED_QUIZ_ENTRY_WIDTH,
                                               c.SET_TIMED_QUIZ_ENTRY_HEIGHT)  # Increased size
        self._entry_time_interval.setFont(c.SET_TIMED_QUIZ_FONT)

        self._label2 = QLabel("Set the number of words per quiz:")
        self._label2.setFont(c.SET_TIMED_QUIZ_FONT)
        self._entry_num_words = QLineEdit("5")
        self._entry_num_words.setFixedSize(c.SET_TIMED_QUIZ_ENTRY_WIDTH,
                                           c.SET_TIMED_QUIZ_ENTRY_HEIGHT)  # Increased size
        self._entry_num_words.setFont(c.SET_TIMED_QUIZ_FONT)
        # Add the labels and entry fields to the layout
        self._layout.addWidget(self._label1)
        self._layout.addWidget(self._entry_time_interval)
        self._layout.addWidget(self._label2)
        self._layout.addWidget(self._entry_num_words)

        # Bottom layout for buttons
        button_layout = QHBoxLayout()
        self._button1 = QPushButton("Set Timed Quiz")
        self._button2 = QPushButton("Go Back")

        self._button1.setFixedSize(c.SET_TIMED_QUIZ_BUTTON_WIDTH,
                                   c.SET_TIMED_QUIZ_BUTTON_HEIGHT)
        self._button1.setFont(c.SET_TIMED_QUIZ_FONT)
        self._button2.setFixedSize(c.SET_TIMED_QUIZ_BUTTON_WIDTH,
                                   c.SET_TIMED_QUIZ_BUTTON_HEIGHT)
        self._button2.setFont(c.SET_TIMED_QUIZ_FONT)
        self._button1.clicked.connect(self._set_timed_quiz)
        self._button2.clicked.connect(self._close_window)

        button_layout.addWidget(self._button1)
        button_layout.addWidget(self._button2)

        # Add button layout to the main layout
        self._layout.addLayout(button_layout)

    def _set_timed_quiz(self) -> None:
        """
        Sets the timed quiz based on user input by calling the open_quiz method in the
        controller, after wards closes the window.

        :return: None
        """
        self._controller.open_quiz(
            self._entry_time_interval.text(),
            self._entry_num_words.text(),
            self._quiz_type.currentText()
        )
        self._close_window()

    def _close_window(self) -> None:
        """
        Closes the current window.

        :return: None
        """
        self.close()
