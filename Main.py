import sys
import threading

from PyQt5.QtWidgets import QApplication, QWidget
import PIL.Image
import pystray
import BasicQuizController
import BasicQuizMenu
import WordFactory
import WordManager as wm
import MainMenuController
import MainMenu as MainMenu

import time

WAIT_TIME_SECONDS = 300


class MainApp:
    """
    the main program, opens the main menu and a timed quiz according to what the user wants

    """
    def __init__(self):
        # self.root = ctk.CTk()
        self.word_manager = wm.WordManager()
        self.scheduler_on=False
        self.scheduler=None
        self.main_menu_on = False
        self.main_menu=None
    def run_main_menu(self):
        self.main_menu_on=True
        print("Running main menu..")
        word_manager=wm.WordManager()
        prog = MainMenuController.MainMenuController(word_manager)
        main_menu=MainMenu.MainMenu(self.root, prog, self.set_quiz_scheduler)

        self.root.mainloop()


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
        tray_thread = threading.Thread(target=self.run_tray)
        tray_thread.start()
        self.run_main_menu_new()
    def minimize(self):
        self.main_menu.hide()
        app = QApplication.instance()
        for widget in app.topLevelWidgets():
            if isinstance(widget, QWidget) and widget is not self:
                widget.hide()
        self.main_menu_on=False
    def run_tray(self):
        image=PIL.Image.open("960x0.webp")
        self.icon=pystray.Icon("david",image,menu=pystray.Menu(
            pystray.MenuItem("Open Vocabulary Builder",self.open_mainmenu_tray)
        ))
        self.icon.run()

    def on_quiz_close(self, quiz_root):
        quiz_root.destroy()
        print("Quiz closed.")

    def run_main_menu_new(self):
        word_manager=wm.WordManager()
        # word_manager.empty_database()
        # word_manager.add_words_from_textfile()

        controller = MainMenuController.MainMenuController(word_manager)
        self.app = QApplication(sys.argv)
        self.main_menu = MainMenu.MainMenu(controller,self.minimize,self.close_program)
        self.main_menu_on=True
        self.main_menu.show()
        sys.exit(self.app.exec_())
    def close_program(self):
        app = QApplication.instance()
        for widget in app.topLevelWidgets():
            if isinstance(widget, QWidget) and widget is not self.main_menu:
                widget.close()
        self.icon.stop()

class TrayIcon:

    def __init__(self):
        pass

if __name__ == "__main__":
    main=MainApp()
    main.run()







