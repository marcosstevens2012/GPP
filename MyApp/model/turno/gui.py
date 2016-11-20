#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plasta.gui import BaseGUI
from model.turno import Turno
from model.turno.add import AddTurno


class TurnoGUI( BaseGUI ):

    def __init__(self, manager, managers = [], parent = None):
        BaseGUI.__init__(self, manager, managers, parent)
        self.loadUI()
        self.DialogAddClass = AddTurno

        self.addFilter(u'Fecha', Turno.fecha)
        self.addFilter(u'Empleado', Turno.empleado)
        self.addFilter(u'Horallegada', Turno.horaLlegada)
        self.addFilter(u'Horasalida', Turno.horaSalida)
        self.addFilter(u'Horas', Turno.horas)
        self.addFilter(u'Producto', Turno.producto)
        self.addFilter(u'Cantidad', Turno.cantidad)

        self.addTableColumn(u'Fecha', Turno.fecha)
        self.addTableColumn(u'Empleado', Turno.empleado)
        self.addTableColumn(u'Horallegada', Turno.horaLlegada)
        self.addTableColumn(u'Horasalida', Turno.horaSalida)
        self.addTableColumn(u'Horas', Turno.horas)
        self.addTableColumn(u'Producto', Turno.producto)
        self.addTableColumn(u'Cantidad', Turno.cantidad)

        self._start_operations()
