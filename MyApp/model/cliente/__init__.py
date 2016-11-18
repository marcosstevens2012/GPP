#!/usr/bin/env python
# -*- coding: utf-8 -*-

from storm.locals import *


class Cliente(object):

    __storm_table__ = "clientes"

    ide = Int(primary = True)
    nombres = Unicode(allow_none = False)
    apellido = Unicode(allow_none = False)
    dni = Unicode(allow_none = False)
    direccion = Unicode()
    telefono = Unicode(allow_none = False)
    edad = Unicode()


    def __init__(self, nombres, apellido, dni, direccion, telefono, edad):
        self.nombres = nombres
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion
        self.telefono = telefono
        self.edad = edad


    def __str__(self):
        return self.nombres
