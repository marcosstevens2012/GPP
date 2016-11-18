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
        ICONFILE = join(abspath(dirname(__file__)),'images_rc/logo.png')
        uic.loadUi(uifile, self)
        self.__centerOnScreen()
        self.setWindowTitle("Gestor de movimientos")
        QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Escape), self, self.close)

        self.managers = managers

    def __centerOnScreen (self):
        resolution = QtGui.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))

   
