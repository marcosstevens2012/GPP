#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plasta.logic.manager import BaseManager
from model.pedidos import Pedidos
from model.cliente import Cliente

class PedidosManager( BaseManager ):

    def __init__(self, store, reset = False, managers = None):
        BaseManager.__init__(self, store, reset)
        self.CLASS = Pedidos
        self.managers = managers
        self._start_operations()


    def obtenerProductosPedido(self, pedido):
        '''
        Retorna la lista de objetos {Pedidoproducto}
        del <pedido> en cuestion
        '''
        from model.pedidoproducto import Pedidoproducto
        return [obj for obj in self.store.find(
            Pedidoproducto,
            Pedidoproducto.pedido == pedido
            )
        ]