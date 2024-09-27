import PIL.Image
import pystray
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout


class TrayBar(QThread):
    close_signal = pyqtSignal()

    def __init__(self, close_program, open_mainmenu):
        super().__init__()
        self.close_program = close_program
        self.icon = self.create_icon(open_mainmenu)

    def create_icon(self, open_mainmenu):
        image = PIL.Image.open("960x0.webp")
        return pystray.Icon("david", image, menu=pystray.Menu(
            pystray.MenuItem("Open Vocabulary Builder", open_mainmenu),
            pystray.MenuItem("Close program", self.close_program_from_tray)
        ))

    def close_program_from_tray(self):
        self.close_signal.emit()

    def run(self):
        self.icon.run()

