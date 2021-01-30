from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit
from PyQt5 import ui
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        ui.loadUi("Profile Page UUpdates.ui", self)

        # find the widgets in the xml file

        self.show()

app = QApplication(sys.argv)
window = UI()
app.exec_()