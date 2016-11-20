#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from gui.mainwindow import MainWindow

from model.seccion.gui import SeccionesGUI
from model.cuenta.gui import CuentasGUI
class Views :

    def __init__(self, models):
        self.managers = models

        app = QtGui.QApplication(sys.argv)
        self.window = MainWindow( self , self.managers)
        self.window.show()
        sys.exit(app.exec_())

    def instanceCliente(self):
        from model.cliente.gui import ClienteGUI
        self.cliente = ClienteGUI(self.managers.clientes, self.managers, parent=self.window)
        return self.cliente

    def instanceEmpleado(self):
        from model.empleado.gui import EmpleadoGUI
        self.empleado = EmpleadoGUI(self.managers.empleados, self.managers, parent=self.window)
        return self.empleado

    def instanceMaquina(self):
        from model.maquina.gui import MaquinaGUI
        self.maquina = MaquinaGUI(self.managers.maquinas, self.managers, parent=self.window)
        return self.maquina

    def instanceMateriaprima(self):
        from model.materiaprima.gui import MateriaprimaGUI
        self.materiaprima = MateriaprimaGUI(self.managers.materiasprimas, self.managers, parent=self.window)
        return self.materiaprima

    def instanceInsumo(self):
        from model.insumos.gui import InsumosGUI
        self.insumos = InsumosGUI(self.managers.insumos, self.managers, parent=self.window)
        return self.insumos

    def instanceProveedor(self):
        from model.proveedor.gui import ProveedorGUI
        self.proveedor = ProveedorGUI(self.managers.proveedores, self.managers, parent=self.window)
        return self.proveedor

    def instanceProducto(self):
        from model.productos.gui import ProductosGUI
        self.productos = ProductosGUI(self.managers.productos, self.managers, parent=self.window)
        return self.productos

    def instancePedidos(self):
        from model.pedidos.gui import PedidosGUI
        self.pedidos_gui = PedidosGUI(self.managers.pedidos, self.managers, parent=self.window)
        return self.pedidos_gui

    def instanceTurnos(self):
        from model.turno.gui import TurnoGUI
        self.turno_gui = TurnoGUI(self.managers.turno, self.managers, parent=self.window)
        return self.turno_gui

    def instanceMovimientos(self):
        from model.movimiento.libro_diario import LibroDiarioGUI
        self.movimientos = LibroDiarioGUI(self.managers.movimientos, managers = [CuentasGUI(self.managers.cuentas)])
        return self.movimientos

    def instanceSecciones(self):
        from model.seccion.secciones_categorias_gui import SeccionesCategoriasGUI
        self.secciones = SeccionesCategoriasGUI(self.managers.secciones, managers =
            [SeccionesGUI(self.managers.secciones, managers = [self.managers.cuentas]),
            CuentasGUI(self.managers.cuentas)])
        return self.secciones
