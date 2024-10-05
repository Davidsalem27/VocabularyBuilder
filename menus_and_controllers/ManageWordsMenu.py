from menus_and_controllers import ManageWordsController
from main.Constants import Constants as c
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel


class ManageWordsMenu(QWidget):
    """
    A GUI for managing words in the Vocabulary Builder application.

    This class provides functionality to add, remove, and display words,
    as well as load words from a local file.

    Fields:
        _controller : Controller for managing word operations.
        _create_show_all_words : Function to create and display the
            menu showing all words.
    """

    def __init__(self, controller: ManageWordsController.ManageWordsController,
                 create_show_all_words: callable) -> None:
        """
        Initializes the ManageWordsMenu with its controller.

        :param controller: Controller for managing word operations.
        :param create_show_all_words: Function to create and display the menu showing all words.
        """
        super().__init__()

        self._show_words_menu = None
        self._controller = controller
        self._create_show_all_words = create_show_all_words
        self.setWindowTitle('Manage Words Menu')
        self.setGeometry(c.MANAGE_WORDS_MENU_POSX, c.MANAGE_WORDS_MENU_POSY,
                         c.MANAGE_WORDS_MENU_WIDTH,c.MANAGE_WORDS_MENU_HEIGHT)

        self._initUI()

    def _initUI(self) -> None:
        """Initializes the user interface components."""
        layout = QVBoxLayout()

        # Input field for user input
        self._input_field = QLineEdit(self)
        self._input_field.setPlaceholderText('Enter word here...')
        layout.addWidget(self._input_field)
        self._input_field.setFixedSize(c.MANAGE_WORDS_MENU_BUTTON_WIDTH,
                                       c.MANAGE_WORDS_MENU_BUTTON_HEIGHT)
        self._input_field.setFont(c.MANAGE_WORDS_BUTTON_FONT)

        # Button to process the input
        self._add_word_button = QPushButton('Add word', self)
        self._add_word_button.clicked.connect(self.add_word)
        layout.addWidget(self._add_word_button)
        self._add_word_button.setFixedSize(c.MANAGE_WORDS_MENU_BUTTON_WIDTH,
                                           c.MANAGE_WORDS_MENU_BUTTON_HEIGHT)
        self._add_word_button.setFont(c.MANAGE_WORDS_BUTTON_FONT)

        # Button to remove a word
        self._clear_button = QPushButton('Remove word', self)
        self._clear_button.clicked.connect(self.remove_word)
        layout.addWidget(self._clear_button)
        self._clear_button.setFixedSize(c.MANAGE_WORDS_MENU_BUTTON_WIDTH,
                                        c.MANAGE_WORDS_MENU_BUTTON_HEIGHT)
        self._clear_button.setFont(c.MANAGE_WORDS_BUTTON_FONT)

        # Button to show all words
        self._show_all_words_button = QPushButton('Show all words', self)
        self._show_all_words_button.clicked.connect(self.open_show_all_words)
        layout.addWidget(self._show_all_words_button)
        self._show_all_words_button.setFixedSize(c.MANAGE_WORDS_MENU_BUTTON_WIDTH,
                                                 c.MANAGE_WORDS_MENU_BUTTON_HEIGHT)
        self._show_all_words_button.setFont(c.MANAGE_WORDS_BUTTON_FONT)

        # Button to delete all words
        self._delete_all_words_button = QPushButton('Delete all the words', self)
        self._delete_all_words_button.clicked.connect(self.delete_all_words)
        layout.addWidget(self._delete_all_words_button)
        self._delete_all_words_button.setFixedSize(c.MANAGE_WORDS_MENU_BUTTON_WIDTH,
                                                   c.MANAGE_WORDS_MENU_BUTTON_HEIGHT)
        self._delete_all_words_button.setFont(c.MANAGE_WORDS_BUTTON_FONT)

        # Button to load from local file
        self._load_local_button = QPushButton('Load From local file', self)
        self._load_local_button.clicked.connect(self.load_local_file)
        layout.addWidget(self._load_local_button)
        self._load_local_button.setFixedSize(c.MANAGE_WORDS_MENU_BUTTON_WIDTH,
                                             c.MANAGE_WORDS_MENU_BUTTON_HEIGHT)
        self._load_local_button.setFont(c.MANAGE_WORDS_BUTTON_FONT)

        # Label to display output
        self._output_label = QLabel('', self)
        layout.addWidget(self._output_label)
        self._output_label.setFixedSize(c.MANAGE_WORDS_MENU_OUTPUT_WIDTH,
                                        c.MANAGE_WORDS_MENU_OUTPUT_HEIGHT) #to change

        self._output_label.setFont(c.MANAGE_WORDS_BUTTON_FONT)

        self.setLayout(layout)

    def delete_all_words(self) -> None:
        """Deletes all words from the database."""
        self._controller.delete_all_words()

    def load_local_file(self) -> None:
        """Loads words from a local file and displays the result."""
        text = self._controller.load_local_file()
        self._output_label.setText(text)

    def add_word(self) -> None:
        """Adds a new word based on user input and displays the result."""
        user_input = self._input_field.text()
        text = self._controller.add_new_word(user_input)
        self._output_label.setText(text)
        self._input_field.clear()

    def remove_word(self) -> None:
        """Removes a word based on user input and displays the result."""
        user_input = self._input_field.text()
        text = self._controller.delete_word(user_input)
        self._output_label.setText(text)
        self._input_field.clear()

    def open_show_all_words(self) -> None:
        """Opens the menu to show all words."""
        self._show_words_menu = self._create_show_all_words()
        self._show_words_menu.show()
