#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date, datetime
from plasta.gui.add import BaseAdd
from PyQt4 import uic, QtGui, QtCore
from plasta.utils.qt import sortListOfListObjs
from plasta.gui.mytablewidget import MyTableWidget
from model.pedidos import Pedidos
from model.pedidoproducto import Pedidoproducto


class AddPedidos( BaseAdd ):

    def __init__(self, manager, itemToEdit = False, managers = [], parent=None):
        BaseAdd.__init__(self, manager, itemToEdit, managers, parent)
        self.loadUI('model/pedidos/uis/add.ui')

        self.linkToAttribute(self.deFecha, Pedidos.fecha)
        self.linkToAttribute(self.cbClientes, Pedidos.cliente)

        self.singleTitle = 'pedido'
        self._start_operations()
        self.loadReferenceCombo(self.cbClientes, Pedidos.cliente, sortAttr='nombres')

        self.objs = {}
        self.productosEnLista = []

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
                    'color':obj.color,
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

        # carga el combo de telas y los productos actuales en la ram
        self.objs['telas'] = sortListOfListObjs(
            self.managers.materiasprimas.get(u'tela'), campo='nombre')

        self.cbTela.clear()
        [self.cbTela.addItem(obj.nombre) for obj in self.objs['telas']]

        # carga el combo de colores y los productos actuales en la ram
        tela = str(self.cbTela.currentIndex())
        self.objs['colores'] = sortListOfListObjs(self.managers.materiasprimas.get(u'tela'), campo='color')

        self.cbColor.clear()
        [self.cbColor.addItem(obj.color) for obj in self.objs['colores']]

    def reloadTableProductos(self):
        cols = [u'Cantidad', u'Producto', u'tela', u'talle', u'color', u'Costo', u'Subtotal']
        self.otwProductos = MyTableWidget(self.twProductos, cols, ['C','L', 'L', 'L', 'L', 'C', 'C'])
        self.otwProductos.fullClear()
        for prod in self.productosEnLista:
            item = [
                prod['cantidad'],
                prod['producto'].producto,
                prod['tela'],
                prod['talle'],
                prod['color'],
                "$ %8.2f" % prod['producto'].costo,
                "$ %8.2f" % prod['subtotal'],
            ]
            self.otwProductos.appendItem(item)
        self.obtenerTotal()

    def obtenerTotal(self):
        total = 0
        for prod in self.productosEnLista:
            total += prod['subtotal']
        self.lbTotal.setText("$ %8.2f" % total)
        return total

    '''def calcularTiempo(self): buscar el tiempo que tarda un empleado en producir una unidad de cada 
    producto seleccionado y en base a eso calcular el tiempo
        
        for prod in self.productosEnLista: 
            tiempo = self.manager.empleados.get(tiempo)
        pass'''

    '''ef calcularDescuento(self): buscar en el historial de pedidos del cliente seleccionado: 
        cantidad de pedidos que hizo hasta el momento y si el monto de estos supera los $X, ofrecer un descuento 
        del X%''' 
    
        

    #REIMPLEMENTED
    def save(self, listData):
        data = {
        'fecha':datetime.strptime(listData[0], "%d/%m/%Y"),
        'cliente':listData[1],
        'estado':u'en_curso',
        'costo':self.obtenerTotal(),
        }
        # guarda el pedido en la bd
        try:
            pedido = self.manager.add(data)
            if not pedido:
                return False

            # se generan los objetos PedidoProducto
            # por cada item de la tabla productos
            for item in self.productosEnLista:
                data = {
                'pedido':pedido,
                'producto':item['producto'],
                'cantidad':item['cantidad'],
                'tela':item['tela'],
                'color':item['color'],
                'precio':item['producto'].costo,
                }
                obj = self.manager.store.add(Pedidoproducto(**data))
            self.manager.store.flush()
            self.manager.store.commit()
            return True
        except Exception as e:
            print e
            return False


###############################################################################

    @QtCore.pyqtSlot()
    def on_btAgregarProducto_clicked(self):
        if self.cbProductos.currentIndex() < 0:
            return

        producto = self.objs['productos'][self.cbProductos.currentIndex()]
        # valida que el producto no se encuentre en la lista
        if producto in [p['producto'] for p in self.productosEnLista]:
            return

        item = {
            'cantidad':self.sbCantidad.value(),
            'talle':self.sbTalle.value(),
            'color':self.cbColor.currentText(), 
            'tela':self.cbTela.currentText(), 
            'producto':producto,
            'subtotal':self.sbCantidad.value() * producto.costo
        }
        self.productosEnLista.append(item)
        self.reloadTableProductos()

    @QtCore.pyqtSlot()
    def on_btQuitarProducto_clicked(self):
        idx = self.otwProductos.widget.currentRow()
        if idx >= 0:
            del self.productosEnLista[idx]
            self.reloadTableProductos()

    @QtCore.pyqtSlot()
    def on_btSave_clicked(self):
        if len(self.productosEnLista) == 0:
            QtGui.QMessageBox.warning(self, self.windowTitle(),
                "No se puede crear un pedido sin productos. Por favor agregue al menos uno.")
            return
        BaseAdd.on_btSave_clicked(self)