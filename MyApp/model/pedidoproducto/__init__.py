#!/usr/bin/env python
# -*- coding: utf-8 -*-

from storm.locals import *
from model.pedidos import Pedidos
from model.productos import Productos


class Pedidoproducto(object):

    __storm_table__ = "pedidoproductos"

    ide = Int(primary = True)
    pedido_int = Int()
    pedido = Reference(pedido_int, Pedidos.ide)
    producto_id = Int()
    producto = Reference(producto_id, Productos.ide)
    cantidad = Int()
    tela = Unicode()
    talle = Int()
    color = Unicode()
    precio = Float()


    def __init__(self, pedido, producto, cantidad, talle, color, tela, precio):
        self.pedido = pedido
        self.producto = producto
        self.cantidad = cantidad
        self.talle = talle 
        self.color = color
        self.tela = tela 
        self.precio = precio


    def __str__(self):
        return u''
