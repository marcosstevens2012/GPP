#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plasta.gui import BaseGUI
from model.productos import Productos
from model.productos.add import AddProductos
from plasta.utils.qt import parseAmount

class ProductosGUI( BaseGUI ):

    def __init__(self, manager, managers = [], parent = None):
        BaseGUI.__init__(self, manager, managers, parent)
        self.loadUI()
        self.DialogAddClass = AddProductos

        self.addFilter(u'Producto', Productos.producto)
        self.addFilter(u'Cantidad', Productos.cantidad)
        self.addFilter(u'Rubro', Productos.rubro)
        self.addFilter(u'Materiaprima', Productos.materiaprima)
        self.addFilter(u'Tiempo', Productos.tiempo)
        self.addTableColumn(u'Producto', Productos.producto)
        self.addTableColumn(u'Cantidad', Productos.cantidad, alignment='C')
        self.addTableColumn(u'Rubro', Productos.rubro)
        self.addTableColumn(u'Costo', Productos.costo, fnParse=parseAmount, alignment='C')
        # self.addTableColumn(u'Insumos', Productos.insumos)
        # self.addTableColumn(u'Materiaprima', Productos.materiaprima)
        # self.addTableColumn(u'Tiempo', Productos.tiempo)

        self.pluralTitle = 'Productos'
        self._start_operations()
