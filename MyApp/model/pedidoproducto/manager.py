#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plasta.logic.manager import BaseManager
from model.pedidoproducto import Pedidoproducto

class PedidoproductoManager( BaseManager ):

    def __init__(self, store, reset = False, managers = None):
        BaseManager.__init__(self, store, reset)
        self.CLASS = Pedidoproducto
        self._start_operations()
