# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from .Ui_main import Ui_MainWindow
import base64


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_btnEncoding_clicked(self):
        """
        Slot documentation goes here.
        """
        txt = self.txtRaw.toPlainText()
        if self.cboxCodecType.currentIndex() == 0:
            encodedStr = base64.b64encode(txt.encode('utf-8'))
        else:
            encodedStr = base64.b16encode(txt.encode('utf-8'))
        self.txtResult.setPlainText(str(encodedStr,'utf-8'))
    
    @pyqtSlot()
    def on_btnDecoding_clicked(self):
        """
        Slot documentation goes here.
        """
        txt = self.txtRaw.toPlainText()
        try:
            if self.cboxCodecType.currentIndex() == 0:
                decodedStr = base64.b64decode(txt.encode('utf-8'))
            else:
                decodedStr = base64.b16decode(txt.encode('utf-8'))
        except Exception as e:
            return
        self.txtResult.setPlainText(str(decodedStr,'utf-8'))
    
    @pyqtSlot()
    def on_btnExchange_clicked(self):
        """
        Slot documentation goes here.
        """
        strRaw = self.txtRaw.toPlainText()
        strResult = self.txtResult.toPlainText()
        self.txtRaw.setPlainText(strResult)
        self.txtResult.setPlainText(strRaw)
