#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plasta.gui.add import BaseAdd
from PyQt4 import uic, QtGui, QtCore
from os.path import join, abspath, dirname
from model.productos import Productos
from model.materiaprima import Materiaprima
from model.insumos import Insumos
from plasta.utils.qt import sortListOfListObjs
from plasta.gui.mytablewidget import MyTableWidget

class AddProductos( BaseAdd ):

    def __init__(self, manager, itemToEdit = False, managers = [], parent =None):
        BaseAdd.__init__(self, manager, itemToEdit, managers)
        self.loadUI('model/productos/add.ui')

        self.linkToAttribute(self.leProducto, Productos.producto)
        self.linkToAttribute(self.sbCantidad, Productos.cantidad)
        self.linkToAttribute(self.leRubro, Productos.rubro)
        self.linkToAttribute(self.dsbCosto, Productos.costo)
        # self.linkToAttribute(self.cbMateriasPrimas, Productos.materiaprima)

        self.addValidator('producto', 'presence')

        self._start_operations()
        # self.loadReferenceCombo(self.cbMateriasPrimas, Productos.materiaprima, sortAttr='nombre')
        #self.loadReferenceCombo(self.cbInsumos, Productos.insumos, sortAttr='nombre')
        # def loadReferenceCombo(self, widget, refAttr, sort=True, sortAttr='nombre'):

        self.objs = {}
        self.materiaprimaEnLista = []

        self.loadWidgets()

    def loadWidgets(self):
        self.objs['materiaprima'] = sortListOfListObjs(self.managers.materiasprimas.getall(), campo='nombre')

        self.cbMateriasPrimas.clear()
        [self.cbMateriasPrimas.addItem(obj.nombre) for obj in self.objs['materiaprima']]
    # @QtCore.pyqtSlot()
    # def on_btSave_clicked(self):
    #     BaseAdd.on_btSave_clicked(self)
    @QtCore.pyqtSlot()
    def on_btAgregarMP_clicked(self):
        if self.cbMateriasPrimas.currentIndex() < 0:
            return

        cantidad = self.sbCantidadMP.value()
        obj = self.objs['materiaprima'][self.cbMateriasPrimas.currentIndex()]
        value = "%s - %s" % (cantidad, obj.nombre)
        self.lwMateriasPrimas.addItem(value)