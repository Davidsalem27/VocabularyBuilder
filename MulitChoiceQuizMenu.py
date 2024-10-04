from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QRadioButton, QPushButton, QMessageBox, QSizePolicy

import MutliChoiceQuizController
from Constants import Constants as c


class MultipleChoiceQuizMenu(QWidget):
    """
    A GUI for managing a multiple-choice quiz.

    This class presents a series of questions, allowing the user to select answers and navigate through them.

    Methods:
        - `__init__(controller: Any, num_questions: int)`: Initializes the quiz menu with a controller and number of questions.
        - `_init_ui() -> None`: Sets up the user interface, displaying the current question and options.
        - `_clear_layout() -> None`: Clears all widgets from the layout.
        - `_display_question() -> None`: Displays the current question and its options.
        - `_check_answer() -> None`: Checks the selected answer and provides feedback.
        - `_next_question() -> None`: Moves to the next question.
        - `_previous_question() -> None`: Moves to the previous question.

    Fields:
        _option_buttons : List of option buttons for the current question.
        _next_button : Button to go to the next question.
        _submit_button : Button to submit the answer.
        _prev_button : Button to go to the previous question.
        _question_label : Label displaying the current question.
        _controller : An instance of the controller to manage quiz logic.
        _questions : List of questions, each containing a word, options, and the index of the correct answer.
        _curr_question_ind : Index of the current question being displayed.
    """

    def __init__(self, controller: MutliChoiceQuizController.MultiChoiceQuizController, num_questions: int):
        """
        Initialize the quiz menu.

        :param controller: The controller to manage quiz logic and state.
        :param num_questions: The number of questions to be displayed in the quiz.

        """
        super().__init__()
        self._option_buttons= []
        self._next_button = None
        self._submit_button = None
        self._prev_button = None
        self._question_label = None
        self.setWindowTitle(c.MULTI_CHOICE_TITLE)
        self.setGeometry(c.MULTI_CHOICE_QUIZ_POSX, c.MULTI_CHOICE_QUIZ_POSY,
                         c.MULTI_CHOICE_QUIZ_WIDTH, c.MULTI_CHOICE_QUIZ_HEIGHT)
        self._layout = QVBoxLayout()
        self._controller = controller
        # self.questions is [(word,[options],ind of correct answer])..]
        self._questions = self._controller.get_questions(num_questions)
        self._curr_question_ind = 0
        self._init_ui()

    def _init_ui(self) -> None:
        """Set up the user interface, displaying the current question and options."""
        self._clear_layout()  # Clear the existing layout
        self._display_question()  # Display the current question

        self._next_button = QPushButton("Next")
        self._next_button.clicked.connect(self._next_question)
        self._next_button.setFixedSize(c.MULTI_CHOICE_QUIZ_WIDTH, c.MULTI_CHOICE_QUIZ_BUTTON_HEIGHT)
        self._next_button.setFont(c.MULTI_CHOICE_BUTTON_FONT)
        self._layout.addWidget(self._next_button)

        self._submit_button = QPushButton("Submit")
        self._submit_button.clicked.connect(self._check_answer)
        self._submit_button.setFixedSize(c.MULTI_CHOICE_QUIZ_WIDTH, c.MULTI_CHOICE_QUIZ_BUTTON_HEIGHT)
        self._submit_button.setFont(c.MULTI_CHOICE_BUTTON_FONT)
        self._layout.addWidget(self._submit_button)

        self._prev_button = QPushButton("Previous")
        self._prev_button.clicked.connect(self._previous_question)
        self._prev_button.setFixedSize(c.MULTI_CHOICE_QUIZ_WIDTH, c.MULTI_CHOICE_QUIZ_BUTTON_HEIGHT)
        self._prev_button.setFont(c.MULTI_CHOICE_BUTTON_FONT)
        self._layout.addWidget(self._prev_button)

        self.setLayout(self._layout)

    def _clear_layout(self) -> None:
        """Clear the layout by deleting existing widgets."""
        for i in reversed(range(self._layout.count())):
            widget = self._layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def _display_question(self) -> None:
        """Display the current question and options."""
        question_text = "What is the meaning of " + self._questions[self._curr_question_ind][0]
        self._question_label = QLabel(question_text)
        self._question_label.setFont(c.MULTI_CHOICE_QUESTION_FONT)
        self._layout.addWidget(self._question_label)

        self._option_buttons = []

        for option in self._questions[self._curr_question_ind][1]:
            button = QRadioButton(option)
            button.setFont(c.MULTI_CHOICE_QUESTION_FONT)
            self._layout.addWidget(button)
            self._option_buttons.append(button)

    def _check_answer(self) -> None:
        """Check the selected answer and provide feedback."""
        selected_option_index = None
        for i, button in enumerate(self._option_buttons):
            if button.isChecked():
                selected_option_index = i
        print(selected_option_index)
        print(self._questions[self._curr_question_ind][2])
        if selected_option_index is not None:
            if selected_option_index == self._questions[self._curr_question_ind][2]:

                self._controller.right_answer(self._questions[self._curr_question_ind][0])
                self._option_buttons[selected_option_index].setText(
                    self._option_buttons[selected_option_index].text() + " ✅")
            else:
                self._option_buttons[selected_option_index].setText(
                    self._option_buttons[selected_option_index].text() + " ❌")

    def _next_question(self) -> None:
        """Move to the next question."""
        if self._curr_question_ind < len(self._questions) - 1:
            self._curr_question_ind += 1
            self._init_ui()

    def _previous_question(self) -> None:
        """Move to the previous question."""
        if self._curr_question_ind > 0:
            self._curr_question_ind -= 1
            self._init_ui()
