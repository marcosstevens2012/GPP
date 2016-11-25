#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date, datetime
from plasta.gui.add import BaseAdd
from PyQt4 import uic, QtGui, QtCore
from plasta.utils.qt import sortListOfListObjs
from plasta.gui.mytablewidget import MyTableWidget
from model.turno import Turno
from model.productos import Productos
from model.empleado import Empleado
from model.pedidos import Pedidos



class AddTurno( BaseAdd ):

    def __init__(self, manager, itemToEdit = False, managers = [], parent=None):
        BaseAdd.__init__(self, manager, itemToEdit, managers, parent)
        self.loadUI('model/turno/add.ui')

        self.linkToAttribute(self.cbEmpleado, Turno.empleado)
        self.linkToAttribute(self.deFecha, Turno.fecha)
        self.linkToAttribute(self.teEntrada, Turno.horaLlegada)
        self.linkToAttribute(self.teSalida, Turno.horaSalida)
        self.linkToAttribute(self.sbHoras, Turno.horas)
        self.linkToAttribute(self.cbProductos, Turno.producto)
        self.linkToAttribute(self.sbCantidad, Turno.cantidad)
        self.linkToAttribute(self.cbPedidos, Turno.pedido)

        self.singleTitle = 'Nuevo Turno'
        self._start_operations()
       
        self.objs = {}
        self.materiaprimaEnLista = []
        self.loadWidgets()

        # si es modo edit
        if itemToEdit:
            # se obtienen y cargan los productos
            # correspondientes al pedido en cuestion
            productos = self.manager.obtenerProductosPedido(itemToEdit)
            # parse los objs para regenerar el formato de la lista de diccionarios
            for obj in productos:
                self.productosEnLista.append({
                    'cantidad':obj.cantidad,
                    'tela': obj.tela,
                    'talle':obj.talle,
                    'producto':obj.producto,
                    'subtotal':obj.precio
                })
            self.reloadTableProductos()

    def loadWidgets(self):
        self.deFecha.setDate(date.today())

        # carga el combo de productos y los productos actuales en la ram
        self.objs['productos'] = sortListOfListObjs(
            self.managers.productos.getall(), campo='producto')

        self.cbProductos.clear()
        [self.cbProductos.addItem(obj.producto) for obj in self.objs['productos']]

        # carga el combo de empleados actuales en la ram
        self.objs['empleados'] = sortListOfListObjs(
            self.managers.empleados.getall(), campo='nombre')

        self.cbEmpleado.clear()
        [self.cbEmpleado.addItem(obj.nombre) for obj in self.objs['empleados']]

           # carga el combo de empleados actuales en la ram
        self.objs['pedidos'] = sortListOfListObjs(
            self.managers.empleados.getall(), campo='ide')

        self.cbPedidos.clear()
        [self.cbPedidos.addItem(str((int(obj.ide)))) for obj in self.objs['pedidos']]
    
  
