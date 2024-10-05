
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget, QScrollArea

from menus_and_controllers import WordMeaningWindow
from main.Constants import Constants as c

class ShowWordsMenu(QWidget):
    """
    Menu for displaying a list of words.
    This widget allows users to view all words in the database and double-click
    on any word to see its meanings in a separate window.

    Attributes:
        _detail_window (WordMeaningWindow): Instance of the window that shows word meanings.
        _controller (Controller): An instance of the controller for managing word retrieval.

    Methods:
        _open_word_detail(item: QListWidgetItem) -> None:
            Opens a new window displaying the meanings of the selected word.
    """

    def __init__(self, controller):
        """
        Initializes the ShowWordsMenu.

        :param controller: An instance of the controller that manages word data.
        """
        super().__init__()
        self._detail_window = None
        self._controller = controller
        self.setWindowTitle('Word List')
        self.setGeometry(c.SHOW_WORDS_MENU_POSX, c.SHOW_WORDS_MENU_POSY,
                         c.SHOW_WORDS_MENU_WIDTH, c.SHOW_WORDS_MENU_HEIGHT)

        self._initUI()

    def _initUI(self) -> None:
        """
        Sets up the user interface for the word list menu.

        Creates a scrollable list of words and connects double-click events
        to the function for displaying word meanings.
        """
        layout = QVBoxLayout()

        # Create a scroll area for the word list
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        # Create a widget to hold the QListWidget
        list_widget_container = QWidget()
        list_layout = QVBoxLayout(list_widget_container)

        # List widget to display words
        self._word_list = QListWidget(self)
        self._word_list.addItems(self._controller.get_all_words())  # get the words

        self._word_list.itemDoubleClicked.connect(self._open_word_detail)
        self._word_list.setFont(c.SHOW_WORDS_MENU_FONT)
        list_layout.addWidget(self._word_list)  # Add the QListWidget to the layout
        list_widget_container.setLayout(list_layout)  # Set the layout for the container
        scroll_area.setWidget(list_widget_container)  # Set the container as the widget of the scroll area
        layout.addWidget(scroll_area)  # Add the scroll area to the main layout
        self.setLayout(layout)

    def _open_word_detail(self, item) -> None:
        """
        Opens a new window displaying the meanings of the selected word.

        :param item: The QListWidgetItem that was double-clicked.
        """
        word = item.text()  # Get the word from the clicked item
        meanings = self._controller.get_meaning(word)
        self._detail_window = WordMeaningWindow.WordMeaningWindow(word, meanings)  # Create a new window for the word
        self._detail_window.show()  # Show the new window
