from plasta.gui.add import BaseAdd
from PyQt4 import uic
from os.path import join, abspath, dirname
from model.turno import Turno

class AddTurno( BaseAdd ):

    def __init__(self, manager, itemToEdit = False, managers = [], parent = None):
        BaseAdd.__init__(self, manager, itemToEdit, managers)
        self.loadUI('model/turno/Add.ui')

########################
# FUNCIONES AUXILIARES #
########################

    def __centerOnScreen (self):
        '''Centers the window on the screen.'''
        resolution = QtGui.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))

    def __toUnicode(self, MyQString):
        return unicode(MyQString.toUtf8(),'utf-8')

    def XXX(self):
        """ """
        pass

############################
# FUNCIONES DE LOS EVENTOS #
############################
    '''@QtCore.pyqtSlot()
    def on_btXXX_clicked(self):
        pass'''

