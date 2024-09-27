import sys


from PyQt5.QtWidgets import QApplication, QWidget
import BasicQuizController
import BasicQuizMenu
import ControllerMenuFactory
import TrayBar

import WordManager as wm




WAIT_TIME_SECONDS = 300


class MainApp:
    """
    the main program, opens the main menu and is responsible for
    minimizing and closing the program

    """
    def __init__(self):
        self.menu_factory=ControllerMenuFactory.ControllerMenuFactory()
        self.app = QApplication(sys.argv)
        self.word_manager = wm.WordManager()
        self.scheduler_on=False
        self.scheduler=None
        self.main_menu_on = False
        self.main_menu=None
        self.tray=None

    def set_quiz_scheduler(self):
        self.scheduler_on=not self.scheduler_on

    def start_quiz(self):

        word_manager = wm.WordManager()
        controller = BasicQuizController.BasicQuizController(word_manager)
        BasicQuizMenu.BasicQuizMenu(None, controller)

    def open_mainmenu_tray(self):
        if not self.main_menu_on:
            self.main_menu.show()

    def run(self):
        self.run_main_menu_new()
        sys.exit(self.app.exec_())
    def minimize(self):
        """
        minimizes the whole program
        :return:
        """
        self.main_menu.hide()
        app = QApplication.instance()
        for widget in app.topLevelWidgets():
            if isinstance(widget, QWidget) and widget is not self:
                widget.hide()
        self.main_menu_on=False


    def create_tray(self):
        self.tray = TrayBar.TrayBar(self.close_program, self.open_mainmenu_tray)
        self.tray.close_signal.connect(self.close_program)  # Connect the signal
        self.tray.start()


    def run_main_menu_new(self):
        self.main_menu=self.menu_factory.create_main_menu(self.minimize,self.close_program)
        self.main_menu_on = True
        self.main_menu.show()
        self.create_tray()

    def close_program(self):
        if self.main_menu:
            self.main_menu.close()
        if self.tray:
            self.tray.quit()
        print("Program closed")
        QApplication.quit()  #close program



if __name__ == "__main__":
    main=MainApp()
    main.run()







