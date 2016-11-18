#!/usr/bin/env python
# -*- coding: utf-8 -*-

from storm.locals import *


class Proveedor(object):

    __storm_table__ = "proveedors"

    id = Int(primary = True)
    nombres = Unicode(allow_none = False)
    apellido = Unicode(allow_none = False)
    dni = Unicode(allow_none = False)
    direccion = Unicode()
    provincia = Unicode()
    ciudad = Unicode()
    email = Unicode()
    telefono = Unicode(allow_none = False)
    observaciones = Unicode()


    def __init__(self, nombres, apellido, dni, direccion, provincia, ciudad, email, telefono, observaciones):
        self.nombres = nombres
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion
        self.provincia = provincia
        self.ciudad = ciudad
        self.email = email
        self.telefono = telefono
        self.observaciones = observaciones


    def __str__(self):
        return u''
