#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plasta.gui.add import BaseAdd
from PyQt4 import uic
from os.path import join, abspath, dirname
from model.maquina import Maquina

class AddMaquina( BaseAdd ):

    def __init__(self, manager, itemToEdit = False, managers = [], parent = None):
        BaseAdd.__init__(self, manager, itemToEdit, managers)
        self.loadUI('model/maquina/add.ui')

    
        self.linkToAttribute(self.leNombre, Maquina.nombre)
        self.linkToAttribute(self.leModel, Maquina.model)
        self.linkToAttribute(self.cbProveedor, Maquina.proveedor)
        self.linkToAttribute(self.cbEstado, Maquina.estado)
        self.linkToAttribute(self.leObservaciones, Maquina.observaciones)

        self._start_operations()
