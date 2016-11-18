#!/usr/bin/env python
# -*- coding: utf-8 -*-

from storm.locals import *


class Empleado(object):

    __storm_table__ = "empleados"

    ide = Int(primary = True)
    nombre = Unicode(allow_none = False)
    #roducto_id = Unicode()
    apellido = Unicode(allow_none = False)
    #tiempo = Unicode()
    direccion = Unicode()
    edad = Unicode()
    sexo = Unicode()
    productividad = Unicode()


    def __init__(self, nombre, apellido, direccion, edad, sexo):
        self.nombre = nombre
        self.apellido = apellido
        #self.tiempo = tiempo
        self.direccion = direccion
        self.edad = edad
        self.sexo = sexo
        


    def __str__(self):
        return u''
