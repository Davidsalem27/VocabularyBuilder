

import Constants as c
import MainMenuController
import ManageWordsMenu
import QuizMenu

import sys
import warnings
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QFont
BUTTON_FONT = QFont("Arial", 30)  # Font family, Font size


class MainMenu(QWidget):
    def __init__(self, controller : MainMenuController,minimize,close_program):
        super().__init__()
        self.controller=controller
        self.words_menu=None
        self.close_program=close_program
        self.setWindowTitle('Vocabulary Builder')
        self.setGeometry(100, 100, 960, 640)


        self.set_background_image('960x0.webp')

        self.button1 = QPushButton('Manage Words', self)
        self.button1.clicked.connect(self.open_words_menu)
        self.button1.setFixedSize(400, 200)
        self.button1.setFont(BUTTON_FONT)
        self.button2 = QPushButton('Quiz yourself!', self)
        self.button2.clicked.connect(self.open_quiz_menu)
        self.button2.setFixedSize(400, 200)
        self.button2.setFont(BUTTON_FONT)
        self.button3 = QPushButton('Other games', self)
        self.button3.clicked.connect(self.function3)
        self.button3.setFixedSize(400, 200)
        self.button3.setFont(BUTTON_FONT)
        self.button4 = QPushButton('Settings', self)
        self.button4.clicked.connect(self.function4)
        self.button4.setFixedSize(400, 200)
        self.button4.setFont(BUTTON_FONT)
        self.button5 = QPushButton('Minimize to tray', self)
        self.button5.clicked.connect(minimize)
        self.button5.setFixedSize(400, 200)
        self.button5.setFont(BUTTON_FONT)
        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)

        self.setLayout(layout)

    def set_background_image(self, image_path):
        oImage = QPixmap(image_path)
        sImage = oImage.scaled(self.size(), aspectRatioMode=1)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

    def close_all_windows(self):
        app = QApplication.instance()
        for widget in app.topLevelWidgets():
            if isinstance(widget, QWidget) and widget is not self:
                widget.close()
    def open_words_menu(self):
        show_words_controller=self.controller.open_words_menu()
        self.words_menu=ManageWordsMenu.ManageWordsMenu(show_words_controller)
        self.words_menu.show()

    def open_quiz_menu(self):
        quiz_menu_controller=self.controller.open_quiz_menu()
        self.quiz_menu=QuizMenu.QuizMenu(quiz_menu_controller)
        self.quiz_menu.show()


    def function3(self):
        print("Set Quiz timer")

    def function4(self):
        print("Settings")

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Close Confirmation', 'Are you sure you want to close the window?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close_program()

            event.accept()
        else:
            event.ignore()  # Ignore the close event
