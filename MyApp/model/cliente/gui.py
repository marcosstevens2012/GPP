#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plasta.gui import BaseGUI
from model.cliente import Cliente
from model.cliente.add import AddCliente


class ClienteGUI( BaseGUI ):

    def __init__(self, manager, managers = [], parent = None):
        BaseGUI.__init__(self, manager, managers, parent)
        self.parent = parent
        self.loadUI()
        self.DialogAddClass = AddCliente

        self.addFilter(u'Nombres', Cliente.nombres)
        self.addFilter(u'Apellido', Cliente.apellido)
        self.addFilter(u'Dni', Cliente.dni)
        self.addFilter(u'Direccion', Cliente.direccion)
        self.addFilter(u'Telefono', Cliente.telefono)
        self.addFilter(u'Edad', Cliente.edad)

        self.addTableColumn(u'Nombres', Cliente.nombres)
        self.addTableColumn(u'Apellido', Cliente.apellido)
        self.addTableColumn(u'Dni', Cliente.dni)
        self.addTableColumn(u'Direccion', Cliente.direccion)
        self.addTableColumn(u'Telefono', Cliente.telefono)
        self.addTableColumn(u'Edad', Cliente.edad)

        self._start_operations()
