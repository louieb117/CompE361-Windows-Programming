from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import pandas as pd
import sys


class UserMain(QMainWindow):
    def __init__(self, ui_file):
        # QMainWindow initialization
        super(UserMain, self).__init__()

        # Load UI file
        uic.loadUi(ui_file, self)
        self.show()
        self.user_window()

    def user_window(self):
        # Debug Message
        print('user')

