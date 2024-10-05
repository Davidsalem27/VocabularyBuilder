# from PIL import ImageQt

from PyQt5 import QtGui

from main.Constants import Constants as c
from menus_and_controllers import MainMenuController
from main import ImageLoader
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QPalette, QBrush, QPixmap


class MainMenu(QWidget):
    """Main menu for the Vocabulary Builder application.

    This class provides buttons for managing words, taking quizzes, accessing settings,
    and minimizing the application.
    currently the settings and othergames options dont do anything

    Fields:
        _controller (MainMenuController): Controller for handling main menu logic.
        _close_program (callable): Function to close the application.
        _create_manage_words_menu (callable): Function to create the manage words menu.
        _create_quiz_menu (callable): Function to create the quiz menu.
        _create_settings_menu (callable): Function to create the settings menu.
    Methods:
        _set_background_image(self, image_path: str) -> None:
            Sets the background image of the main menu.

        _open_words_menu(self) -> None:
            Opens the manage words menu.

        _open_quiz_menu(self) -> None:
            Opens the quiz menu.

        _open_settings(self) -> None:
            Opens the settings menu.

        _function3(self) -> None:
            Placeholder for additional functionality.

        closeEvent(self, event) -> None:
            Handles the close event to confirm exit.
    """

    def __init__(self, controller: MainMenuController, minimize: callable, close_program: callable,
                 create_manage_words_menu: callable, create_quiz_menu: callable,
                 create_settings_menu: callable) -> None:
        """Initializes the main menu with buttons and layout.

        :param controller: Controller for handling main menu logic.
        :param minimize: Function to minimize the main window.
        :param close_program: Function to close the application.
        :param create_manage_words_menu: Function to create the manage words menu.
        :param create_quiz_menu: Function to create the quiz menu.
        :param create_settings_menu: Function to create the settings menu.
        """
        super().__init__()
        self._quiz_menu = None
        self._controller = controller
        self._words_menu = None
        self._minimize = minimize
        self._close_program = close_program
        self._create_manage_words_menu = create_manage_words_menu
        self._create_quiz_menu = create_quiz_menu
        self._create_settings_menu = create_settings_menu
        self.setWindowTitle(c.TITLE_MAIN_MENU)
        self.setGeometry(c.MAIN_MENU_POSX, c.MAIN_MENU_POSY,
                         c.MAIN_MENU_WIDTH, c.MAIN_MENU_HEIGHT)

        self._set_background_image(c.MAIN_MENU_IMAGE_PATH)
        self.init_ui()  # Call to initialize UI components

    def init_ui(self) -> None:
        """Initializes the UI components including buttons and layout."""
        self._button1 = QPushButton('Manage Words', self)
        self._button1.clicked.connect(self._open_words_menu)
        self._button1.setFixedSize(c.MAIN_MENU_BUTTON_WIDTH,c.MAIN_MENU_BUTTON_HEIGHT)
        self._button1.setFont(c.BUTTON_FONT)

        self._button2 = QPushButton('Quiz yourself!', self)
        self._button2.clicked.connect(self._open_quiz_menu)
        self._button2.setFixedSize(c.MAIN_MENU_BUTTON_WIDTH,c.MAIN_MENU_BUTTON_HEIGHT)
        self._button2.setFont(c.BUTTON_FONT)

        self._other_games_button = QPushButton('Other games', self)
        self._other_games_button.clicked.connect(self._other_games)
        self._other_games_button.setFixedSize(c.MAIN_MENU_BUTTON_WIDTH, c.MAIN_MENU_BUTTON_HEIGHT)
        self._other_games_button.setFont(c.BUTTON_FONT)

        # self._setting_button = QPushButton('Settings', self)
        # self._setting_button.clicked.connect(self._open_settings)
        # self._setting_button.setFixedSize(c.MAIN_MENU_BUTTON_WIDTH, c.MAIN_MENU_BUTTON_HEIGHT)
        # self._setting_button.setFont(c.BUTTON_FONT)

        self._button5 = QPushButton('Minimize to tray', self)
        self._button5.clicked.connect(self._minimize)
        self._button5.setFixedSize(c.MAIN_MENU_BUTTON_WIDTH,c.MAIN_MENU_BUTTON_HEIGHT)
        self._button5.setFont(c.BUTTON_FONT)

        layout = QVBoxLayout()
        layout.addWidget(self._button1)
        layout.addWidget(self._button2)
        layout.addWidget(self._other_games_button)
        # layout.addWidget(self._setting_button)
        layout.addWidget(self._button5)

        self.setLayout(layout)

    def _set_background_image(self, image_path: str) -> None:
        """Sets the background image of the main menu.

        :param image_path: Path to the background image file.
        :return: None
        """
        oImage = QPixmap(image_path)
        sImage = oImage.scaled(self.size(), aspectRatioMode=1)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

    def _open_words_menu(self) -> None:
        """Opens the manage words menu.

        :return: None
        """
        self._words_menu = self._create_manage_words_menu()
        self._words_menu.show()

    def _open_quiz_menu(self) -> None:
        """Opens the quiz menu.

        :return: None
        """
        self._quiz_menu = self._create_quiz_menu()
        self._quiz_menu.show()

    def _open_settings(self) -> None:
        """Opens the settings menu.
        there is the base of an implementation of this feature for future needs
        but right now it does nothing
        :return: None
        """
        self.settings_menu = self._create_settings_menu()
        self.settings_menu.show()

    def _other_games(self) -> None:
        """Placeholder for additional functionality.
        :return: None
        """
        pass

    def closeEvent(self, event) -> None:
        """Handles the close event to confirm exit.

        :param event: The close event.
        :return: None
        """
        reply = QMessageBox.question(self, 'Close Confirmation', 'Are you sure you want to close the program?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
            self._close_program()
        else:
            event.ignore()
