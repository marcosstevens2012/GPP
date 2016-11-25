#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plasta.logic.manager import BaseManager
from model.turno import Turno

class TurnoManager( BaseManager ):

    def __init__(self, store, reset = False, managers = None ):
        BaseManager.__init__(self, store, reset)
        self.CLASS = Turno
        self.managers = managers
        self._start_operations()
