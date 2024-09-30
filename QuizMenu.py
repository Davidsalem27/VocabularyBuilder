from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
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

        function2() -> None:
            Placeholder for additional functionality.

        _open_set_time_quiz() -> None:
            Opens the timed quiz menu.
    """

    def __init__(self, controller: QuizMenuController.QuizMenuController,
                 create_basic_quiz: callable,
                 create_timed_quiz_menu: callable):
        """
        Initializes the QuizMenu with the specified controller and menu creation functions.

        :param controller: The controller managing quiz logic.
        :param create_basic_quiz: Callable to create the basic quiz menu.
        :param create_timed_quiz_menu: Callable to create the timed quiz menu.
        """
        super().__init__()
        self._basic_quiz = None
        self._set_menu = None
        self._create_timed_quiz_menu = create_timed_quiz_menu
        self._create_basic_quiz = create_basic_quiz
        self.setWindowTitle('Quiz Menu')
        self.setGeometry(c.QUIZ_MENU_POSX, c.QUIZ_MENU_POSY,
                         c.QUIZ_MENU_WIDTH, c.QUIZ_MENU_HEIGHT)


        self._controller = controller
        self._initUI()

    def _initUI(self) -> None:
        """Initializes the user interface components."""
        layout = QVBoxLayout()

        # Label to display output
        self._output_label = QLabel('Click a button to see the action.', self)
        layout.addWidget(self._output_label)

        # Button 1
        self._button1 = QPushButton('Start Basic Quiz', self)
        self._button1.clicked.connect(self._open_basic_quiz_menu)
        self._button1.setFixedSize(c.QUIZ_MENU_BUTTON_WIDTH,c.QUIZ_MENU_BUTTON_HEIGHT)
        self._button1.setFont(c.QUIZ_MENU_BUTTON_FONT)
        layout.addWidget(self._button1)

        # Button 2
        self._button2 = QPushButton('Start Basic Quiz 2', self)
        self._button2.clicked.connect(self.function2)
        self._button2.setFixedSize(c.QUIZ_MENU_BUTTON_WIDTH,c.QUIZ_MENU_BUTTON_HEIGHT)
        self._button2.setFont(c.QUIZ_MENU_BUTTON_FONT)
        layout.addWidget(self._button2)

        # Button 3
        self._button3 = QPushButton('Set Timed Quiz', self)
        self._button3.clicked.connect(self._open_set_time_quiz)
        self._button3.setFixedSize(c.QUIZ_MENU_BUTTON_WIDTH,c.QUIZ_MENU_BUTTON_HEIGHT)
        self._button3.setFont(c.QUIZ_MENU_BUTTON_FONT)
        layout.addWidget(self._button3)

        self.setLayout(layout)

    def _open_basic_quiz_menu(self) -> None:
        """Opens the basic quiz menu."""
        self._basic_quiz = self._create_basic_quiz()
        self._basic_quiz.show()

    def function2(self) -> None:
        """Placeholder for additional functionality."""
        self._output_label.setText('Function 2 was called!')

    def _open_set_time_quiz(self) -> None:
        """Opens the timed quiz menu."""
        self._set_menu = self._create_timed_quiz_menu()
        self._set_menu.show()
