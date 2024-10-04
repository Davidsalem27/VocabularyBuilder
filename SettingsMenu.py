from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QCheckBox, QLineEdit, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
import sys

class SettingsMenu(QWidget):
    def __init__(self,controller):
        super().__init__()
        self.setWindowTitle("Checkboxes with Separate Functions")
        self.setGeometry(100, 100, 300, 400)
        self.controller=controller
        layout = QVBoxLayout()

        # Checkbox 1
        self.checkbox1 = QCheckBox("full screen mode", self)
        self.checkbox1.stateChanged.connect(self.checkbox_one_changed)
        layout.addWidget(self.checkbox1)


        # Checkbox 2
        self.checkbox2 = QCheckBox("Label 2", self)
        self.checkbox2.stateChanged.connect(self.checkbox_two_changed)
        layout.addWidget(self.checkbox2)

        # Checkbox 3
        self.checkbox3 = QCheckBox("Label 3", self)
        self.checkbox3.stateChanged.connect(self.checkbox_three_changed)
        layout.addWidget(self.checkbox3)

        # Checkbox 4
        self.checkbox4 = QCheckBox("Label 4", self)
        self.checkbox4.stateChanged.connect(self.checkbox_four_changed)
        layout.addWidget(self.checkbox4)

        # Checkbox 5
        self.checkbox5 = QCheckBox("Label 5", self)
        self.checkbox5.stateChanged.connect(self.checkbox_five_changed)
        layout.addWidget(self.checkbox5)



        self.setLayout(layout)

    def checkbox_one_changed(self, state):
        if state == Qt.Checked:
            pass
        else:
            pass

    def checkbox_two_changed(self, state):
        if state == Qt.Checked:
            pass
        else:
            pass

    def checkbox_three_changed(self, state):
        if state == Qt.Checked:
            pass
        else:
            pass

    def checkbox_four_changed(self, state):
        if state == Qt.Checked:
            pass
        else:
            pass

    def checkbox_five_changed(self, state):
        if state == Qt.Checked:
            pass
        else:
            pass


