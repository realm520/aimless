# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from ui.main import *


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    sys.exit(app.exec_())
