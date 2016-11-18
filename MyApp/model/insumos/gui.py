#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plasta.gui import BaseGUI
from model.insumos import Insumos
from model.insumos.add import AddInsumos


class InsumosGUI( BaseGUI ):

    def __init__(self, manager, managers = [], parent = None):
        BaseGUI.__init__(self, manager, managers, parent)
        self.loadUI()
        self.DialogAddClass = AddInsumos

        self.addFilter(u'Nombre', Insumos.nombre)
        self.addFilter(u'Costo', Insumos.costo)
        self.addFilter(u'Cantidad', Insumos.cantidad)
        self.addFilter(u'Minimo', Insumos.minimo)
        self.addFilter(u'Maximo', Insumos.maximo)
        self.addFilter(u'Stock', Insumos.stock)

        self.addTableColumn(u'Nombre', Insumos.nombre)
        self.addTableColumn(u'Costo', Insumos.costo)
        self.addTableColumn(u'Cantidad', Insumos.cantidad)
        self.addTableColumn(u'Minimo', Insumos.minimo)
        self.addTableColumn(u'Maximo', Insumos.maximo)
        self.addTableColumn(u'Stock', Insumos.stock)

        self._start_operations()
