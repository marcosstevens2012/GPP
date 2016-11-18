#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plasta.gui import BaseGUI
from model.proveedor import Proveedor
from model.proveedor.add import AddProveedor


class ProveedorGUI( BaseGUI ):

    def __init__(self, manager, managers = [], parent = None):
        BaseGUI.__init__(self, manager, managers, parent)
        self.loadUI()
        self.DialogAddClass = AddProveedor

        self.addFilter(u'Nombres', Proveedor.nombres)
        self.addFilter(u'Apellido', Proveedor.apellido)
        self.addFilter(u'Dni', Proveedor.dni)
        self.addFilter(u'Direccion', Proveedor.direccion)
        self.addFilter(u'Provincia', Proveedor.provincia)
        self.addFilter(u'Ciudad', Proveedor.ciudad)
        self.addFilter(u'Email', Proveedor.email)
        self.addFilter(u'Telefono', Proveedor.telefono)
        self.addFilter(u'Observaciones', Proveedor.observaciones)

        self.addTableColumn(u'Nombres', Proveedor.nombres)
        self.addTableColumn(u'Apellido', Proveedor.apellido)
        self.addTableColumn(u'Dni', Proveedor.dni)
        self.addTableColumn(u'Direccion', Proveedor.direccion)
        self.addTableColumn(u'Provincia', Proveedor.provincia)
        self.addTableColumn(u'Ciudad', Proveedor.ciudad)
        self.addTableColumn(u'Email', Proveedor.email)
        self.addTableColumn(u'Telefono', Proveedor.telefono)
        self.addTableColumn(u'Observaciones', Proveedor.observaciones)

        self._start_operations()
