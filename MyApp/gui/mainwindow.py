#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from PyQt4 import QtCore, QtGui, uic
from os.path import join, abspath, dirname
from model.movimiento.libro_diario import LibroDiarioGUI
from model.seccion.secciones_categorias_gui import SeccionesCategoriasGUI
from model.seccion.gui import SeccionesGUI
from model.cuenta.gui import CuentasGUI
from model.cliente.gui import ClienteGUI
from model.empleado.gui import EmpleadoGUI
from model.maquina.gui import MaquinaGUI
#from model.pedidos.gui import PedidosGUI
from model.proveedor.gui import ProveedorGUI
from model.materiaprima.gui import MateriaprimaGUI
from model.productos.gui import ProductosGUI
from model.insumos.gui import InsumosGUI

class MainWindow(QtGui.QMainWindow):

    def __init__(self, views, managers = None):
        QtGui.QMainWindow.__init__(self)
        FILENAME = 'mainwindow.ui'
        uifile = join(abspath(dirname(__file__)), FILENAME)
        uic.loadUi(uifile, self)
        QtGui.QShortcut( QtGui.QKeySequence( QtCore.Qt.Key_Escape ), self, self.close )
        self.__centerOnScreen()
        self.setWindowTitle("MVC Struct - Example Plasta App")

        self.views = views
        self.managers = managers

    def __centerOnScreen (self):
        '''Centers the window on the screen.'''
        resolution = QtGui.QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
                  (resolution.height() / 2) - (self.frameSize().height() / 2))

    @QtCore.pyqtSlot()
    def on_btClientes_clicked(self):
        window = self.views.instanceCliente()
        window.show()

    @QtCore.pyqtSlot()
    def on_btEmpleados_clicked(self):
        window = self.views.instanceEmpleado()
        window.show()

    @QtCore.pyqtSlot()
    def on_btMaquinas_clicked(self):
        window = self.views.instanceMaquina()
        window.show()

    @QtCore.pyqtSlot()
    def on_btMp_clicked(self):
        window = self.views.instanceMateriaprima()
        window.show()

    @QtCore.pyqtSlot()
    def on_btInsumos_clicked(self):
        window = self.views.instanceInsumo()
        window.show()

    @QtCore.pyqtSlot()
    def on_btProductos_clicked(self):
        window = self.views.instanceProducto()
        window.show()

    @QtCore.pyqtSlot()
    def on_btProveedores_clicked(self):
        window = self.views.instanceProveedor()
        window.show()

    @QtCore.pyqtSlot()
    def on_btMovimientos_clicked(self):
        window = self.views.instanceMovimientos()
        window.show()

    @QtCore.pyqtSlot()
    def on_btCuentas_clicked(self):
        window = self.views.instanceSecciones()
        window.show()

    @QtCore.pyqtSlot()
    def on_btPedidos_clicked(self):
        window = self.views.instancePedidos()
        window.show()

