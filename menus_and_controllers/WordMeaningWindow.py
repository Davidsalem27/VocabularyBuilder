from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea

from main.Constants import Constants as c
class WordMeaningWindow(QWidget):
    """
    Window for displaying the details and meanings of a specific word.

    This widget shows the selected word along with its meanings and examples.

    Attributes:
        _word (str): The word whose details are being displayed.
        _meanings (list[tuple]): A list of tuples containing meanings and examples of the word.

    Methods:
        _init_ui() -> None:
            Initializes the user interface for displaying word details.
    """

    def __init__(self, word: str, meanings: list[tuple[str, str]]) -> None:
        """
        Initializes the WordMeaningWindow.

        :param word: The word to display details for.
        :param meanings: A list of tuples where each tuple contains a meaning and an example.
        """
        super().__init__()
        self.setWindowTitle('Word Detail')
        self.setGeometry(c.WORD_MEANING_WINDOW_POSX, c.WORD_MEANING_WINDOW_POSY,
                         c.WORD_MEANING_WINDOW_WIDTH, c.WORD_MEANING_WINDOW_HEIGHT)

        self._word = word
        self._meanings = meanings
        self._init_ui()

    def _init_ui(self) -> None:
        """
        Sets up the user interface for displaying the word details.

        Creates a layout with a scrollable area to display the meanings and examples of the word.
        """
        layout = QVBoxLayout()
        layout.addWidget(QLabel(f'Details for: {self._word}'))  # Display the word details
        self.setLayout(layout)

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        scroll_content = QWidget()  # Create a content widget for the scroll area
        scroll_layout = QVBoxLayout(scroll_content)

        # Adding meanings and examples to the layout
        for index, (meaning, example) in enumerate(self._meanings):
            meaning_label = QLabel(f"{index + 1}. {meaning}", self)
            meaning_label.setWordWrap(True)
            meaning_label.setFont(c.WORD_MEANING_FONT)
            scroll_layout.addWidget(meaning_label)

            if example:
                example_label = QLabel(f"   Example: {example}", self)
                example_label.setWordWrap(True)
                example_label.setFont(c.WORD_MEANING_FONT)
                scroll_layout.addWidget(example_label)

            # Add spacing between meanings
            scroll_layout.addSpacing(20)

        scroll_area.setWidget(scroll_content)  # Set the content widget in the scroll area
        layout.addWidget(scroll_area)  # Add the scroll area to the main layout

        self.setLayout(layout)
