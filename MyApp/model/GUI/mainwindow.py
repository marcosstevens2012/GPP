#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from PyQt4 import QtCore, QtGui, uic
import images_rc
from os.path import join,abspath,dirname


class MainWindow(QtGui.QMainWindow):

    def __init__(self, managers = None):
        FILENAME = 'mainwindow.ui'
        QtGui.QMainWindow.__init__(self)
        uifile = os.path.join(os.path.abspath(os.path.dirname(__file__)),FILENAME)
        uic.loadUi(uifile, self)
        self.__centerOnScreen()
        self.setWindowTitle("Gestor de movimientos")
        QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Escape), self, self.close)

        self.managers = managers

    

   
