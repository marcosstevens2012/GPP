#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plasta.logic.manager import BaseManager
from model.materiaprima import Materiaprima

class MateriaprimaManager( BaseManager ):

    def __init__(self, store, reset = False , managers = None):
        BaseManager.__init__(self, store, reset)
        self.CLASS = Materiaprima
        self._start_operations()
