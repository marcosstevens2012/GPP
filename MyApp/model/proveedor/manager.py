#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plasta.logic.manager import BaseManager
from model.proveedor import Proveedor

class ProveedorManager( BaseManager ):

    def __init__(self, store, reset = False, managers = None ):
        BaseManager.__init__(self, store, reset)
        self.CLASS = Proveedor
        self.managers = managers
        self._start_operations()
