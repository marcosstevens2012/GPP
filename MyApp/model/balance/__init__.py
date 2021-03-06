#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path

class Balance ():

    def __init__(self):
        self.pathFile = "model/movimiento/data.dll"

    def actualizar(self, unMonto, tipo):
        monto_actual = self.valor()
        balance = open(self.pathFile,'w')
        monto_nuevo = 0
        if tipo == u'Ingreso' :
            monto_nuevo = monto_actual + unMonto
        else:
            monto_nuevo = monto_actual - unMonto
        balance.write(str(monto_nuevo))
        balance.close()

    def valor(self):
        if not os.path.exists(self.pathFile) :
            balance = open(self.pathFile,'w')
            balance.write("0")
            balance.close()
        balance = open(self.pathFile,'r')
        try:
            monto_actual = float(balance.readline())
        except ValueError:
            monto_actual = 0
        balance.close()
        return monto_actual

    def cuentasIngreso(self, cuentas):
        balance = 0
        for cuenta in cuentas :
            balance += float( cuenta.monto )
        return balance

    def cuentasEgreso(self, cuentas):
        balance = 0
        for cuenta in cuentas :
            balance += float( cuenta.monto )
        return balance
