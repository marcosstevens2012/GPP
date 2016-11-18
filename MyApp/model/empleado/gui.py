#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plasta.gui import BaseGUI
from model.empleado import Empleado
from model.empleado.add import AddEmpleado


class EmpleadoGUI( BaseGUI ):

    def __init__(self, manager, managers = [], parent = None):
        BaseGUI.__init__(self, manager, managers, parent)
        self.loadUI()
        self.DialogAddClass = AddEmpleado

        self.addFilter(u'Nombre', Empleado.nombre)
        self.addFilter(u'Apellido', Empleado.apellido)
        self.addFilter(u'Direccion', Empleado.direccion)
        self.addFilter(u'Edad', Empleado.edad)
        self.addFilter(u'Sexo', Empleado.sexo)
        self.addFilter(u'Productividad', Empleado.productividad)

        self.addTableColumn(u'Nombre', Empleado.nombre)
        self.addTableColumn(u'Apellido', Empleado.apellido)
        self.addTableColumn(u'Direccion', Empleado.direccion)
        self.addTableColumn(u'Edad', Empleado.edad)
        self.addTableColumn(u'Sexo', Empleado.sexo)
        self.addTableColumn(u'Productividad', Empleado.productividad)

        self._start_operations()
