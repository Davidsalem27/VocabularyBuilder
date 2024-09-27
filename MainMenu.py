from PyQt5.QtCore import QTimer

import Constants as c
import MainMenuController
import ManageWordsMenu
import QuizMenu

import sys
import warnings
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QFont

import SettingsMenu


class MainMenu(QWidget):
    def __init__(self, controller : MainMenuController,minimize,close_program,
                 create_manage_words_menu,create_quiz_menu,create_settings_menu):
        super().__init__()
        self.quiz_menu = None
        self.controller=controller
        self.words_menu=None
        self.close_program=close_program
        self.create_manage_words_menu=create_manage_words_menu
        self.create_quiz_menu=create_quiz_menu
        self.create_settings_menu=create_settings_menu
        self.setWindowTitle('Vocabulary Builder')
        self.setGeometry(100, 100, 960, 640)


        self.set_background_image('960x0.webp')

        self.button1 = QPushButton('Manage Words', self)
        self.button1.clicked.connect(self.open_words_menu)
        self.button1.setFixedSize(400, 200)
        self.button1.setFont(c.BUTTON_FONT)
        self.button2 = QPushButton('Quiz yourself!', self)
        self.button2.clicked.connect(self.open_quiz_menu)
        self.button2.setFixedSize(400, 200)
        self.button2.setFont(c.BUTTON_FONT)
        self.button3 = QPushButton('Other games', self)
        self.button3.clicked.connect(self.function3)
        self.button3.setFixedSize(400, 200)
        self.button3.setFont(c.BUTTON_FONT)
        self.button4 = QPushButton('Settings', self)
        self.button4.clicked.connect(self.open_settings)
        self.button4.setFixedSize(400, 200)
        self.button4.setFont(c.BUTTON_FONT)
        self.button5 = QPushButton('Minimize to tray', self)
        self.button5.clicked.connect(minimize)
        self.button5.setFixedSize(400, 200)
        self.button5.setFont(c.BUTTON_FONT)
        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.set_quiz_timer)  # Connect the timeout signal to the update_time method


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
        self.words_menu=self.create_manage_words_menu()
        self.words_menu.show()

    def open_quiz_menu(self):
        self.quiz_menu=self.create_quiz_menu()
        self.quiz_menu.show()
    def open_settings(self):
        self.settings_menu=self.create_settings_menu()

        self.settings_menu.show()

    def function3(self):
        print("Set Quiz timer")

    def start_timer(self):
        print("Settings")
        self.timer.start(5000)
        # self.time_label.setText("Timer started")
    def set_quiz_timer(self):
        quiz_menu_controller = self.controller.open_quiz_menu()
        self.quiz_menu = QuizMenu.QuizMenu(quiz_menu_controller)
        self.quiz_menu.open_basic_quiz_menu()
    def stop_timer(self):
        self.timer.stop()  # Stop the timer

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Close Confirmation', 'Are you sure you want to close the program?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
            self.close_program()
        else:
            event.ignore()
