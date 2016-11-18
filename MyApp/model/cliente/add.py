#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plasta.gui.add import BaseAdd
from PyQt4 import uic
from os.path import join, abspath, dirname
from model.cliente import Cliente

class AddCliente( BaseAdd ):

    def __init__(self, manager, itemToEdit = False, managers = [], parent = None):
        BaseAdd.__init__(self, manager, itemToEdit, managers)
        self.loadUI('model/cliente/add.ui')

        self.linkToAttribute(self.leNombres, Cliente.nombres)
        self.linkToAttribute(self.leApellido, Cliente.apellido)
        self.linkToAttribute(self.leDni, Cliente.dni)
        self.linkToAttribute(self.leDireccion, Cliente.direccion)
        self.linkToAttribute(self.leTelefono, Cliente.telefono)
        self.linkToAttribute(self.leEdad, Cliente.edad)
        
        self._start_operations()
        self.leNombres.textEdited.connect(lambda text: self.leNombres.setText(text.toUpper()))
