#!/usr/bin/env python
# -*- coding: utf-8 -*-


from model.cliente.manager import ClienteManager
from model.empleado.manager import EmpleadoManager
from model.maquina.manager import MaquinaManager
from model.materiaprima.manager import MateriaprimaManager
from model.insumos.manager import InsumosManager
from model.pedidos.manager import PedidosManager
from model.productos.manager import ProductosManager
from model.pedidoproducto.manager import PedidoproductoManager
from model.proveedor.manager import ProveedorManager
from model.movimiento.manager import MovimientosManager
from model.cuenta.manager import CuentasManager
from model.seccion.manager import SeccionesManager
from model.turno.manager import TurnoManager



class Models:

    def __init__(self, controller):
        self.controller = controller

        store = controller.store

        vReset = False
        self.clientes = ClienteManager(store, reset = vReset, managers = self)
        self.empleados = EmpleadoManager(store, reset = vReset, managers = self)
        self.maquinas = MaquinaManager(store, reset = vReset, managers = self)
        self.materiasprimas = MateriaprimaManager(store, reset = vReset, managers = self)
        self.insumos = InsumosManager(store, reset = vReset, managers = self)
        self.productos = ProductosManager(store, reset = vReset, managers = self)
        self.proveedores = ProveedorManager(store, reset = vReset, managers = self)
        self.cuentas = CuentasManager(store, reset = vReset)
        self.movimientos = MovimientosManager(store, reset = vReset)
        self.secciones = SeccionesManager(store, reset = vReset, managers = self)
        self.pedidos = PedidosManager(store, reset = vReset, managers = self)
        self.pedidoproductos = PedidoproductoManager(store, reset = vReset, managers = self)
        self.turno = TurnoManager(store, reset = vReset, managers = self)


