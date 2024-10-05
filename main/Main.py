
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from menus_and_controllers import ControllerMenuFactory
from main import TrayBar



class MainApp:
    """
    The main program, opens the main menu,the tray icon and is responsible for
    minimizing and closing the program.

    Fields:
        _menu_factory (ControllerMenuFactory): Factory to create menu controllers.
        _app (QApplication): The main application instance.
        main_menu (QWidget): Reference to the main menu widget.
        tray (TrayBar): Reference to the system tray icon.

    Methods:
        __init__(self) -> None: Initializes the main application and its components.
        _create_tray(self) -> None: Creates the system tray icon and connects signals.
        _run_main_menu(self) -> None: Creates and shows the main menu.
        close_program(self) -> None: Closes the application and its components.
        open_mainmenu_tray(self) -> None: Opens the main menu from the system tray.
        run(self) -> None: Runs the application, displaying the main menu and system tray.
        minimize(self) -> None: Minimizes the whole program to be used by a button.
    """

    def __init__(self) -> None:
        """Initializes the main application and its components."""
        self._menu_factory = ControllerMenuFactory.ControllerMenuFactory()
        self._app = QApplication(sys.argv)

        self._main_menu_on = False
        self._main_menu = None
        self._tray = None

    def _create_tray(self) -> None:
        """Creates the system tray icon and connects signals.

        :return: None
        """
        self._tray = TrayBar.TrayBar(self.open_mainmenu_tray)
        self._tray.close_signal.connect(self.close_program)  # Connect the signal
        self._tray.start()

    def _run_main_menu(self) -> None:
        """Creates and shows the main menu.

        :return: None
        """
        self._main_menu = self._menu_factory.create_main_menu(self.minimize, self.close_program)
        self._main_menu_on = True
        self._main_menu.show()

    def close_program(self) -> None:
        """Closes the application and its components.

        :return: None
        """
        if self._main_menu:
            self._main_menu.close()
        if self._tray:
            self._tray.quit()
        QApplication.quit()  # Close program

    def open_mainmenu_tray(self) -> None:
        """Opens the main menu, to be used from the system tray.

        :return: None
        """
        if not self._main_menu_on:
            self._main_menu.show()

    def run(self) -> None:
        """Runs the application, displaying the main menu and system tray.

        :return: None
        """
        self._run_main_menu()
        self._create_tray()
        sys.exit(self._app.exec_())

    def minimize(self) -> None:
        """Minimizes the whole program.

        :return: None
        """
        self._main_menu.hide()
        app = QApplication.instance()
        for widget in app.topLevelWidgets():
            if isinstance(widget, QWidget) and widget is not self:
                widget.hide()
        self._main_menu_on = False


if __name__ == "__main__":
    main = MainApp()
    main.run()
