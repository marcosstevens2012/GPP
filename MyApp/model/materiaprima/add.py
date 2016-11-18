#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plasta.gui.add import BaseAdd
from PyQt4 import uic
from os.path import join, abspath, dirname
from model.materiaprima import Materiaprima

class AddMateriaprima( BaseAdd ):

    def __init__(self, manager, itemToEdit = False, managers = [], parent = None):
        BaseAdd.__init__(self, manager, itemToEdit, managers)
        self.loadUI('model/materiaprima/add.ui')

        self.linkToAttribute(self.leNombre, Materiaprima.nombre)
        self.linkToAttribute(self.dsbCosto, Materiaprima.costo)
        self.linkToAttribute(self.leStock, Materiaprima.stock)
        self.linkToAttribute(self.sbStockminimo, Materiaprima.stockminimo)
        self.linkToAttribute(self.leColor, Materiaprima.color)
        self.linkToAttribute(self.leCategoria, Materiaprima.categoria)

        self._start_operations()
