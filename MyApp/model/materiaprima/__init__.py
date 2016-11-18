#!/usr/bin/env python
# -*- coding: utf-8 -*-

from storm.locals import *


class Materiaprima(object):

    __storm_table__ = "materiaprimas"

    ide = Int(primary = True)
    nombre = Unicode(allow_none = False)
    costo = Float()
    stock = Int()
    stockminimo = Int()
    color = Unicode()
    categoria = Unicode()


    def __init__(self, nombre, costo, stock, stockminimo, color, categoria):
        self.nombre = nombre
        self.costo = costo
        self.stock = stock
        self.stockminimo = stockminimo
        self.color = color
        self.categoria = categoria


    def __str__(self):
        return u''
