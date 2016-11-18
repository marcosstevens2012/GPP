#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plasta.gui import BaseGUI
from model.maquina import Maquina
from model.maquina.add import AddMaquina


class MaquinaGUI( BaseGUI ):

    def __init__(self, manager, managers = [], parent = None):
        BaseGUI.__init__(self, manager, managers, parent)
        self.loadUI()
        self.DialogAddClass = AddMaquina

       
        self.addFilter(u'Nombre', Maquina.nombre)
        self.addFilter(u'Model', Maquina.model)
        self.addFilter(u'Proveedor', Maquina.proveedor)
        self.addFilter(u'Estado', Maquina.estado)
        self.addFilter(u'Productividad', Maquina.productividad)
        self.addFilter(u'Observaciones', Maquina.observaciones)

        
        self.addTableColumn(u'Nombre', Maquina.nombre)
        self.addTableColumn(u'Model', Maquina.model)
        self.addTableColumn(u'Proveedor', Maquina.proveedor)
        self.addTableColumn(u'Estado', Maquina.estado)
        self.addTableColumn(u'Productividad', Maquina.productividad)
        self.addTableColumn(u'Observaciones', Maquina.observaciones)

        self._start_operations()
