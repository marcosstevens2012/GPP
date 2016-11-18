#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plasta.gui.add import BaseAdd
from PyQt4 import uic
from os.path import join, abspath, dirname
from model.insumos import Insumos

class AddInsumos( BaseAdd ):

    def __init__(self, manager, itemToEdit = False, managers = [], parent = None):
        BaseAdd.__init__(self, manager, itemToEdit, managers)
        self.loadUI('model/insumos/add.ui')

        self.linkToAttribute(self.leNombre, Insumos.nombre)
        self.linkToAttribute(self.leCosto, Insumos.costo)
        self.linkToAttribute(self.leCantidad, Insumos.cantidad)
        self.linkToAttribute(self.leMinimo, Insumos.minimo)
        self.linkToAttribute(self.leMaximo, Insumos.maximo)
        self.linkToAttribute(self.leStock, Insumos.stock)

        self._start_operations()
