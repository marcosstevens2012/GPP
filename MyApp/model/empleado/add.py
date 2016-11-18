#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plasta.gui.add import BaseAdd
from PyQt4 import uic
from os.path import join, abspath, dirname
from model.empleado import Empleado
from plasta.utils.qt import sortListOfListObjs
from plasta.gui.mytablewidget import MyTableWidget
from model.pedidos import Pedidos
from model.pedidoproducto import Pedidoproducto

class AddEmpleado( BaseAdd ):

    def __init__(self, manager, itemToEdit = False, managers = [], parent = None):
        BaseAdd.__init__(self, manager, itemToEdit, managers)
        self.loadUI('model/empleado/add.ui')

        self.linkToAttribute(self.leNombre, Empleado.nombre)
        self.linkToAttribute(self.leApellido, Empleado.apellido)
        self.linkToAttribute(self.leDireccion, Empleado.direccion)
        self.linkToAttribute(self.leEdad, Empleado.edad)
        self.linkToAttribute(self.leSexo, Empleado.sexo)
        

        self._start_operations()
        self.objs = {}
        self.loadWidgets()



    def loadWidgets(self):

        # carga el combo de productos y los productos actuales en la ram
        self.objs['productos'] = sortListOfListObjs(
            self.managers.productos.getall(), campo='producto')

        self.cbProductos.clear()
        [self.cbProductos.addItem(obj.producto) for obj in self.objs['productos']]
