#!/usr/bin/env python
# -*- coding: utf-8 -*-

from storm.locals import *


class Maquina(object):

    __storm_table__ = "maquinas"

    ide = Int(primary = True)
    nombre = Unicode (allow_none = False)
    model = Unicode (allow_none = False)
    proveedor = Unicode()
    estado = Unicode()
    productividad = Unicode()
    observaciones = Unicode()


    def __init__(self, nombre, model, proveedor, estado, productividad, observaciones):
        self.nombre = nombre
        self.model = model
        self.proveedor = proveedor
        self.estado = estado
        self.productividad = productividad
        self.observaciones = observaciones


    def __str__(self):
        return u''
