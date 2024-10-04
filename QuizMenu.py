from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QSlider
from Constants import Constants as c
import QuizMenuController


class QuizMenu(QWidget):
    """
    Quiz menu for navigating between different quiz types.

    This class provides options to start basic quizzes and set a timed quiz.

    Fields:
        _controller: The controller managing quiz logic.
        _create_basic_quiz: Callable to create the basic quiz menu.
        _create_timed_quiz_menu: Callable to create the timed quiz menu.
        _basic_quiz: Optional reference to the basic quiz menu.
        _set_menu: Optional reference to the timed quiz menu.

    Methods:
        _initUI() -> None:
            Initializes the user interface components.

        _open_basic_quiz_menu() -> None:
            Opens the basic quiz menu.

        _open_multichoice_quiz() -> None:
            Opens the multichoice quiz menu.

        _open_set_time_quiz() -> None:
            Opens the timed quiz menu.
    """

    def __init__(self, controller: QuizMenuController.QuizMenuController,
                 create_basic_quiz: callable,
                 create_timed_quiz: callable,
                 create_multichoice_quiz: callable):
        """
        Initializes the QuizMenu with the specified controller and menu creation functions.

        :param controller: The controller managing quiz logic.
        :param create_basic_quiz: Callable to create the basic quiz menu.
        :param create_multichoice_quiz: Callable to create the multichoice quiz menu.
        :param create_timed_quiz: Callable to create the timed quiz menu.
        """
        super().__init__()
        self._multichoice_quiz = None
        self._basic_quiz = None
        self._set_menu = None
        self._create_multichoice_quiz = create_multichoice_quiz
        self._create_timed_quiz_menu = create_timed_quiz
        self._create_basic_quiz = create_basic_quiz
        self.setWindowTitle('Quiz Menu')
        self.setGeometry(c.QUIZ_MENU_POSX, c.QUIZ_MENU_POSY,
                         c.QUIZ_MENU_WIDTH, c.QUIZ_MENU_HEIGHT)

        self._controller = controller
        self._initUI()

    def _initUI(self) -> None:
        """Initializes the user interface components."""
        layout = QVBoxLayout()

        # Button 1
        self._basic_quiz_button = QPushButton('Start Basic Quiz', self)
        self._basic_quiz_button.clicked.connect(self._open_basic_quiz_menu)
        self._basic_quiz_button.setFixedSize(c.QUIZ_MENU_BUTTON_WIDTH, c.QUIZ_MENU_BUTTON_HEIGHT)
        self._basic_quiz_button.setFont(c.QUIZ_MENU_BUTTON_FONT)
        layout.addWidget(self._basic_quiz_button)

        # Button 2
        self._button2 = QPushButton('Start Multiple Choice Quiz', self)
        self._button2.clicked.connect(self._open_multichoice_quiz)
        self._button2.setFixedSize(c.QUIZ_MENU_BUTTON_WIDTH,
                                   c.QUIZ_MENU_BUTTON_HEIGHT)
        self._button2.setFont(c.QUIZ_MENU_BUTTON_FONT)
        layout.addWidget(self._button2)

        self._slider = QSlider()
        self._slider.setOrientation(Qt.Horizontal)
        self._slider.setMinimum(c.QUIZ_MENU_MIN_WORDS)
        self._slider.setMaximum(c.QUIZ_MENU_MAX_WORDS)
        self._slider.setSingleStep(1)  # increment by 1
        self._slider.setFixedSize(c.QUIZ_MENU_SLIDER_WIDTH,
                                  c.QUIZ_MENU_SLIDER_HEIGHT)
        self._slider.setFont(c.QUIZ_MENU_BUTTON_FONT)
        self._slider.valueChanged.connect(self._slider_change_label)

        # Label to show the current state
        self._slider_label = QLabel("Number of words in quiz: " + str(c.QUIZ_MENU_MIN_WORDS))
        self._slider_label.setFixedSize(c.QUIZ_MENU_BUTTON_WIDTH,
                                        c.QUIZ_MENU_BUTTON_HEIGHT)
        self.setFont(c.QUIZ_MENU_BUTTON_FONT)
        # Add slider and label to the layout
        layout.addWidget(self._slider)
        layout.addWidget(self._slider_label)

        # Button 3
        self._button3 = QPushButton('Set Timed Quiz', self)
        self._button3.clicked.connect(self._open_set_time_quiz)
        self._button3.setFixedSize(c.QUIZ_MENU_BUTTON_WIDTH, c.QUIZ_MENU_BUTTON_HEIGHT)
        self._button3.setFont(c.QUIZ_MENU_BUTTON_FONT)
        layout.addWidget(self._button3)

        self.setLayout(layout)

    def _slider_change_label(self, value: int) -> None:
        """
        function that updates the label to the current value of slider
        :param value: the current value
        :return: None
        """
        self._slider_label.setText(f"Number of words in quiz: {value}")

    def _open_basic_quiz_menu(self) -> None:
        """Opens the basic quiz menu."""
        self._basic_quiz = self._create_basic_quiz(self._slider.value())
        self._basic_quiz.show()

    def _open_multichoice_quiz(self) -> None:
        """Placeholder for additional functionality."""
        self._multichoice_quiz = self._create_multichoice_quiz(self._slider.value())
        self._multichoice_quiz.show()

    def _open_set_time_quiz(self) -> None:
        """Opens the timed quiz menu."""
        self._set_menu = self._create_timed_quiz_menu()
        self._set_menu.show()
