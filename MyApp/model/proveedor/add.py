#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plasta.gui.add import BaseAdd
from PyQt4 import uic
from os.path import join, abspath, dirname
from model.proveedor import Proveedor

class AddProveedor( BaseAdd ):

    def __init__(self, manager, itemToEdit = False, managers = [], parent = None):
        BaseAdd.__init__(self, manager, itemToEdit, managers)
        self.loadUI('model/proveedor/add.ui')

        self.linkToAttribute(self.leNombres, Proveedor.nombres)
        self.linkToAttribute(self.leApellido, Proveedor.apellido)
        self.linkToAttribute(self.leDni, Proveedor.dni)
        self.linkToAttribute(self.leDireccion, Proveedor.direccion)
        self.linkToAttribute(self.leProvincia, Proveedor.provincia)
        self.linkToAttribute(self.leCiudad, Proveedor.ciudad)
        self.linkToAttribute(self.leEmail, Proveedor.email)
        self.linkToAttribute(self.leTelefono, Proveedor.telefono)
        self.linkToAttribute(self.leObservaciones, Proveedor.observaciones)

        self._start_operations()
