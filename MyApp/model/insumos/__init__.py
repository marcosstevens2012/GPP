#!/usr/bin/env python
# -*- coding: utf-8 -*-

from storm.locals import *


class Insumos(object):

    __storm_table__ = "insumos"

    id = Int(primary = True)
    
    nombre = Unicode(allow_none = False)
    costo = Unicode(allow_none = False)
    cantidad = Unicode()
    minimo = Unicode()
    maximo = Unicode()
    stock = Unicode()


    def __init__(self, nombre, costo, cantidad, minimo, maximo, stock):
        self.nombre = nombre
        self.costo = costo
        self.cantidad = cantidad
        self.minimo = minimo
        self.maximo = maximo
        self.stock = stock


    def __str__(self):
        return u''
