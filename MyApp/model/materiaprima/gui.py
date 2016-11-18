#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plasta.gui import BaseGUI
from model.materiaprima import Materiaprima
from model.materiaprima.add import AddMateriaprima


class MateriaprimaGUI( BaseGUI ):

    def __init__(self, manager, managers = [], parent = None):
        BaseGUI.__init__(self, manager, managers, parent)
        self.loadUI()
        self.DialogAddClass = AddMateriaprima

        self.addFilter(u'Nombre', Materiaprima.nombre)
        self.addFilter(u'Costo', Materiaprima.costo)
        self.addFilter(u'Stock', Materiaprima.stock)
        self.addFilter(u'Stockminimo', Materiaprima.stockminimo)
        self.addFilter(u'Color', Materiaprima.color)
        self.addFilter(u'Categoria', Materiaprima.categoria)

        self.addTableColumn(u'Nombre', Materiaprima.nombre)
        self.addTableColumn(u'Costo', Materiaprima.costo)
        self.addTableColumn(u'Stock', Materiaprima.stock)
        self.addTableColumn(u'Stockminimo', Materiaprima.stockminimo)
        self.addTableColumn(u'Color', Materiaprima.color)
        self.addTableColumn(u'Categoria', Materiaprima.categoria)

        self._start_operations()
