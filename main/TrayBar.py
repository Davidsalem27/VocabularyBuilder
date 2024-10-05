import PIL.Image
import pystray
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout
from main.Constants import Constants as c

class TrayBar(QThread):
    """A class that manages a system tray icon for the application.

    This class creates a system tray icon with options to open the main menu
    and close the application. It runs in a separate thread to avoid blocking
    the main application.

    Attributes:
        close_signal (pyqtSignal): Signal emitted to indicate that the program should close.

    Methods:

        close_program_from_tray() -> None:
            Emits a signal to indicate that the program should close.
        run() -> None:
            Runs the tray icon, allowing it to be displayed and interacted with in the system tray.
    """

    close_signal = pyqtSignal()

    def __init__(self, open_mainmenu: callable) -> None:
        """Initializes the TrayBar with functions to close the program and open the main menu.

        :param open_mainmenu: Function to open the main menu.
        """
        super().__init__()
        self._icon = self._create_icon(open_mainmenu)

    def _create_icon(self, open_mainmenu: callable) -> pystray.Icon:
        """Creates the system tray icon with menu options.

        :param open_mainmenu: Function to open the main menu.
        :return: The created tray icon.
        """
        image = PIL.Image.open(c.TRAY_IMAGE_PATH)
        return pystray.Icon("david", image, menu=pystray.Menu(
            pystray.MenuItem("Open Vocabulary Builder", open_mainmenu),
            pystray.MenuItem("Exit program", self.close_program_from_tray)
        ))

    def close_program_from_tray(self) -> None:
        """Emits a signal to indicate that the program should close.

        This method is called when the "Close program" option is selected from the tray menu.
        """
        self.close_signal.emit()

    def run(self) -> None:
        """Runs the tray icon, allowing it to be displayed and interacted with in the system tray.

        This method is executed in a separate thread to keep the application responsive.
        """
        self._icon.run()
