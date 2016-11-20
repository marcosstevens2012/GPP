#!/usr/bin/env python
# -*- coding: utf-8 -*-

from storm.locals import *
from model.cliente import Cliente
from model.productos import Productos
from model.materiaprima import Materiaprima

class Pedidos(object):

    __storm_table__ = "pedidos"

    ide = Int(primary = True)
    fecha = Date(allow_none = False)
    cliente_id = Int()
    materiaprima_id = Int()
    cliente = Reference(cliente_id, Cliente.ide)
    talle = Int()
    tela = Reference(materiaprima_id, Materiaprima.categoria)
    costo = Float()
    estado = Unicode(allow_none = False)
    fechafin = Date()


    def __init__(self, fecha, cliente, talle, tela, costo, estado=None, fechafin=None):
        self.fecha = fecha
        self.cliente = cliente
        self.talle = talle
        tela.tela = tela 
        self.costo = costo
        self.estado = estado
        self.fechafin = fechafin


    def __str__(self):
        return self.fecha

