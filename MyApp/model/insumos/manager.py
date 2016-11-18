#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plasta.logic.manager import BaseManager
from model.insumos import Insumos

class InsumosManager( BaseManager ):

    def __init__(self, store, reset = False, managers = None ):
        BaseManager.__init__(self, store, reset)
        self.CLASS = Insumos
        self._start_operations()
