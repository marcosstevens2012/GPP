#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plasta.gui import BaseGUI
from model.pedidos import Pedidos
from model.pedidos.add import AddPedidos
from plasta.utils.qt import parseAmount, parseDt2St

class PedidosGUI( BaseGUI ):

    def __init__(self, manager, managers = [], parent = None):
        BaseGUI.__init__(self, manager, managers, parent)
        self.loadUI()
        self.DialogAddClass = AddPedidos

        self.addFilter(u'Cliente', Pedidos.cliente)
        self.addFilter(u'Costo', Pedidos.costo)
        self.addFilter(u'Estado', Pedidos.estado)
        self.addFilter(u'Fechafin', Pedidos.fechafin)

        self.addTableColumn(u'Fecha', Pedidos.fecha, alignment='C', fnParse=parseDt2St)
        self.addTableColumn(u'Cliente', Pedidos.cliente)
        self.addTableColumn(u'Costo', Pedidos.costo, alignment='C', fnParse=parseAmount)
        self.addTableColumn(u'Estado', Pedidos.estado)
        self.addTableColumn(u'Fecha fin', Pedidos.fechafin)

        self.pluralTitle = 'Pedidos'
        self._start_operations()
