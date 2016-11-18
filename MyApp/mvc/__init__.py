#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mvc.controller import Controller
from mvc.models import Models
from mvc.views import Views


class Main :

    def __init__(self):
        self.controller = Controller()
        self.models = Models( self.controller )

        # self._cargarFakeClientes(10)
        # self._cargarFakeProductos(10)

        self.views = Views( self.models )



    def _cargarFakeClientes(self, cantidad):
        import random

        for i in range(cantidad):
            value = str(i + 1)
            item = {
            'nombres':u'Nombre%s' % value,
            'apellido':u'Apellido%s' % value,
            'dni':unicode(random.randint(20000000, 40000000)),
            'direccion':u'Direccion%s' % value,
            'telefono':u'Telefono%s' % value,
            'edad':u'',
            }
            print 'agregando cliente %s/%s...' % (value, cantidad)
            self.models.clientes.add(item)

    def _cargarFakeProductos(self, cantidad):
        import random

        for i in range(cantidad):
            value = str(i + 1)
            item = {
            'producto':u'Producto%s' % value,
            'cantidad':0,
            'costo':random.randint(200, 2000),
            'rubro':u'',
            }
            print 'agregando producto %s/%s...' % (value, cantidad)
            self.models.productos.add(item)
