# -*- encoding: utf-8 -*-
import os
import sys
from PyQt4 import QtCore, QtGui, uic
from storm.locals import *
from plasta.config import config
from storm.locals import create_database, Store
import conexion
import sqlite3
from cliente.manager import ClienteManager
from cliente.gui import ClienteGUI
from cliente.add import AddCliente
from plasta.gui import BaseGUI

#from producto.add import AddProducto

# Cargar nuestro archivo .ui
form_class = uic.loadUiType("Pedido.ui")[0]
 
class PedidoGUI(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
  



    def on_btPedidos_clicked(self):
        #query para buscar por nombre en caso de que no se escriba nada en el campo se muestran todos los datos
        query = unicode("SELECT * FROM clientes WHERE nombres LIKE \"%{0}%\"").format(unicode(self.buscar_cliente.text()))
        #se ejecuta el query y se almacena en una valriable
        datos_obtenidos = conexion.consultas(query)
        if len(datos_obtenidos) == 0:
            query = unicode("SELECT * FROM clientes WHERE dni LIKE \"%{0}%\"").format(unicode(self.buscar_cliente.text()))
            datos_obtenidos = conexion.consultas(query)
        else:
            pass
        #se toma la longitud de la consulta realizada y se asigna a una variable global para usarla en otros metodos
        self.datos = len(datos_obtenidos)
        #se asignan el numero de columnas para la tabla
        self.twLista.setColumnCount(5)
        #se asignan el numero de filas para la tabla dado la longitud de la consulta
        self.twLista.setRowCount(len(datos_obtenidos))
        #bucle para llenar la tabla por fila
        for fila in xrange(len(datos_obtenidos)):
            #bucle para llenar la tabla por columna
            for columna in xrange(5):
                #se crea un item
                item = QtGui.QTableWidgetItem()
                #se le asigna el valor a enviar
                item.setText("%s" %(unicode(datos_obtenidos[fila][columna])))
                #se envia el valor a la tabla por posición fila columna
                self.twLista.setItem(fila, columna, item)



    def on_abm_clientes_clicked(self):
        DATABASE = create_database('sqlite:abm.db')
        almacen = Store(DATABASE)
        cm = ClienteManager(almacen, reset = False)
        self.cliente = AddCliente(manager = cm, managers = [])
        self.cliente.show()

    def on_abm_productos_clicked(self):
        DATABASE = create_database('sqlite:abm.db')
        almacen = Store(DATABASE)
        cm = ClienteManager(productos, reset = False)
        self.productos = AddProductos(manager = cm, managers = [])
        #self.cliente.setWindowIcon( self.btLibroDiario.icon() )
        self.productos.show()


    
