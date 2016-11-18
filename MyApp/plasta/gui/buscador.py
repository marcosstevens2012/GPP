#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       Copyright 2012 Fernandez, Emiliano <emilianohfernandez@gmail.com>
#       Copyright 2012 Ferreyra, Jonathan <jalejandroferreyra@gmail.com>
#
#       Informática MEG <contacto@informaticameg.com>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import sys
from PyQt4 import QtCore, QtGui
from plasta.gui import BaseGUI
from plasta.config import config


class BaseSearcher(QtGui.QDialog, BaseGUI):

    def __init__(self,manager, dict_referencias = None):
        QtGui.QDialog.__init__(self)
        self.loadUI('/plasta/gui/buscador.ui')

        self.ATRI_COMBO_BUSQUEDA = []#el orden y la cantidad de atributos en str que quieras
        self.ATRIBUTOSLISTA = []#el orden y la cantidad de atributos en str que quieras
        self.alignmentColumns = []
        self.fnParseTableItem = None

        self.ATRIBUTOSLISTA_CLASSNAMES = []
        self.manager = manager
        self.dict_referencias = dict_referencias
        self.objetoSeleccionado = None
        self.fnsParseListAttrs = []
        self.fnAllItems = self.manager.getall
        self.fnFilterItems = None
        self.widgets = {
            'btNew':True, 'btEdit':True, 'btDelete':True,
            'leSearch':True, 'cbFilters':True,
            'twItems':True, 'lbItemsCount':True,
            'lbTitle':True
        }
        # Single title to show in gui
        self.singleTitle = self.manager.getClassName()
        # Plural title to show in gui
        self.pluralTitle = self.manager.getClassName()

        self.lang = config().LANG
        self.messages = {
            'es':{
                'new':'Nuevo',
                'edit':'Editar',
                'delete':'Eliminar',
                'deleteConfirm':u"¿Está seguro que desea eliminar?.\n\n",
                'itemsCount':' item(s) listado(s)',
                'search':'Buscar',
                'filters':'Filtros'
            },
            'en':{
                'new':'New',
                'edit':'Edit',
                'delete':'Delete',
                'deleteConfirm':u"¿Are you sure?.\n\n",
                'itemsCount':' item(s) listed',
                'search':'Search',
                'filters':'Filters'
            }
        }
        self._operaciones_de_inicio()

    @QtCore.pyqtSlot()
    def on_btAceptar_clicked(self):
        objeto = self.actualRowsToObjects()[0]
        if self.dict_referencias :
            clave = [k for k, v in self.dict_referencias.iteritems() if v == None][0]
            self.dict_referencias[clave] = objeto
            clave.setText(objeto.__str__())
        else:
            self.objetoSeleccionado = objeto
        self.close()

    def on_twDatos_doubleClicked(self , index):
        self.on_btAceptar_clicked()

    #===================================================================
    # Metodos de Logica
    #===================================================================

    def _operaciones_de_inicio(self):
        u'''
        operaciones necesarias para levantar las ventanas
        '''
        self.lbTitle.setText(self.manager.getClassName())
        self.makeTable()
        self.loadCombobox()
        self.loadTable()
        self.loadShortcuts()
        self.fullScreen = False
        # self._centerOnScreen()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Escape), self, self.close)

    def loadShortcuts(self):
        u""" Load shortcuts used in the application. """
        QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Escape), self, self.close)
        self._atajo_salir = QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Q"), self, self.close)