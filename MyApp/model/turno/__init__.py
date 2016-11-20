#!/usr/bin/env python
# -*- coding: utf-8 -*-

from storm.locals import *
from model.empleado import Empleado
from model.pedidos import Pedidos 
from model.productos import Productos 


class Turno(object):

    __storm_table__ = "turnos"

    ide = Int(primary = True)
    empleado_id = Int()
    pedido_id = Int()
    producto_id = Int()
    fecha = Date()
    empleado = Reference(empleado_id, Empleado.ide)
    horaLlegada = Unicode()
    horaSalida = Unicode()
    horas = Int()
    producto = Reference(producto_id, Productos.ide)
    pedido = Reference (pedido_id, Pedidos.ide)
    cantidad = Int(allow_none = False)


    def __init__(self, fecha, empleado, horaLlegada, horaSalida, horas, producto, cantidad):
        self.fecha = fecha
        self.empleado = empleado
        self.horaLlegada = horaLlegada
        self.horaSalida = horaSalida
        self.horas = horas
        self.producto = producto
        self.cantidad = cantidad


    def __str__(self):
        return u''
