#!/usr/bin/env python
# -*- coding: utf-8 -*-

from storm.locals import *
from model.materiaprima import Materiaprima
from model.insumos import Insumos


class Productos(object):

    __storm_table__ = "productoss"

    id = Int(primary = True)
    producto = Unicode(allow_none = False)
    cantidad = Int()
    rubro = Unicode()
    materiaprima_id = Int()
    materiaprima = Reference(materiaprima_id, Materiaprima.ide)
    tiempo = Unicode()
    costo = Float()


    def __init__(self, producto, cantidad, rubro, costo, tiempo=u'', insumos=None, materiaprima=None):
        self.producto = producto
        self.cantidad = cantidad
        self.rubro = rubro
        self.materiaprima = materiaprima
        self.tiempo = tiempo
        self.costo = costo


    def __str__(self):
        return self.producto
