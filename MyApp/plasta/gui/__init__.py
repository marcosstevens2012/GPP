#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import join, abspath, dirname
from PyQt4 import QtCore, QtGui, uic
from plasta.gui.mytablewidget import MyTableWidget
from plasta.utils import pathtools
from plasta.utils.qt import centerOnScreen, setStyle
from plasta.config import config

class BaseGUI( QtGui.QMainWindow ):
    '''Base class to handle operations of CRUD screen'''

    def __init__(self, manager, managers = None, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        # Name file of ui for gui
        self.parent = parent
        self.FILENAME = '/plasta/gui/uis/list.ui'
        self.processEvents = QtGui.QApplication.processEvents
        self.develop = config.DEVELOP

        # Name file of icon window
        self.ICONFILE = ''
        #
        self.manager = manager
        #
        self.managers = managers

        # ATRIBUTOSLISTA: lista de diccionarios donde puedes indicar el orden y formato
        # en que se deben mostrar los atributos en la lista. Siendo la clave del diccionario,
        # el texto en Unicode del texto que tendra la cabecera de la columna. Y el valor contenido
        # en el mismo elemento, el atributo de la clase que se mostrara en esa columna
        # Ejemplo:
        # self.ATRIBUTOSLISTA = [ {u'Nombres':Cliente.Nombres}, {u'Domicilio':Cliente.Domicilio}]
        self.ATRIBUTOSLISTA = []

        # ATRI_COMBO_BUSQUEDA: lista de diccionarios donde puedes indicar el orden de como
        # quieres que se muestren y vean los atributos en el combo de los filtros
        # El formato es el mismo que <ATRIBUTOSLISTA>
        self.ATRI_COMBO_BUSQUEDA = []#el orden y la cantidad de atributos en str que quieras

        # Use this if you need parse attributes in list
        # Format {listOfList}: [[index, function], ...]
        # Params function: fn(row, currentValue)
        # Use: [[0, lambda (row, value): value.uppper()], ...]
        self.fnsParseListAttrs = []

        #
        self.fnAllItems = self.manager.getall
        #
        self.fnFilterItems = None

        # funcion para parsear los items de la tabla
        self.fnParseTableItem = None

        # Alignment of each atttribute in the list
        # Possible values: C = CENTER, L = LEFT, R = RIGHT
        # Use: self.alignmentColumns = ['C', 'L', 'R', 'L']
        self.alignmentColumns = []

        # List of objects current are listeds
        self.items = []

        self.widgets = {
            'btNew':True, 'btEdit':True, 'btDelete':True,
            'leSearch':False, 'cbFilters':True,
            'twItems':True, 'lbItemsCount':True,
            'lbTitle':True
        }
        # DialogAddClass: reference to the class to instantiate to
        # handle dialog window add / edit
        self.DialogAddClass = None

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

    def _start_operations( self ):
        '''Operations necessary to display the window'''
        self.processEvents = QtGui.QApplication.processEvents
        self.fullScreen = False
        self.lang = config().LANG
        self.translateWidgets()
        self.makeTable()
        self.processEvents()
        self.loadCombobox()
        self.loadTable()
        self.processEvents()
        self.loadShortcuts()
        centerOnScreen(self)
        setStyle(self)
        self.processEvents()
        if self.widgets['btEdit']:
            self.btEdit.setVisible(False)
        if self.widgets['btDelete']:
            self.btDelete.setVisible(False)

        # self.setWindowIcon( QtGui.QIcon( QtGui.QPixmap( join( abspath( dirname( __file__ ) ), self.ICONFILE ) ) ) )
        if self.widgets['lbTitle']:
            self.lbTitle.setText(self.pluralTitle)
        self.setWindowTitle(self.pluralTitle)

    def loadUI(self, pathToFile = None):
        from plasta.utils.qt import loadUI
        loadUI(self, pathToFile)

    def getMsgByLang(self, msg):
        return self.messages[self.lang][msg]

    def translateWidgets(self):
        if self.widgets['btNew']:
            self.btNew.setText(self.getMsgByLang('new'))
        if self.widgets['btEdit']:
            self.btEdit.setText(self.getMsgByLang('edit'))
        if self.widgets['btDelete']:
            self.btDelete.setText(self.getMsgByLang('delete'))
        if self.widgets['leSearch']:
            self.lbSearch.setText(self.getMsgByLang('search'))
        if self.widgets['cbFilters']:
            self.lbFilters.setText(self.getMsgByLang('filters'))

    def toogleFullScreen( self ):
        ''' '''
        if not self.fullScreen :
            self.showFullScreen()
        else:
            self.showNormal()
        self.fullScreen = not self.fullScreen

    def loadShortcuts( self ):
        u""" Load shortcuts used in the application. """
        self._atajo_salir = QtGui.QShortcut( QtGui.QKeySequence( "Ctrl+Q" ), self, self.close )
        self._atajo_fullscreen = QtGui.QShortcut( QtGui.QKeySequence( "F11" ), self, self.toogleFullScreen )
        QtGui.QShortcut( QtGui.QKeySequence( QtCore.Qt.Key_Escape ), self, self.close )

        if self.widgets['btNew']:
            QtGui.QShortcut( QtGui.QKeySequence( QtCore.Qt.CTRL | QtCore.Qt.Key_N ), self, self.on_btNew_clicked )
        if self.widgets['btEdit']:
            QtGui.QShortcut( QtGui.QKeySequence( QtCore.Qt.CTRL | QtCore.Qt.Key_M ), self, self.on_btEdit_clicked )
        if self.widgets['btDelete']:
            QtGui.QShortcut( QtGui.QKeySequence( "Del" ), self, self.on_btDelete_clicked )

    def makeTable( self ):
        '''Create the structure of table (columns)'''
        if not self.ATRIBUTOSLISTA :
            tableColumns = [p.capitalize() for p in self._get_attributes_names()]
        else:
            self.ATRIBUTOSLISTA_CLASSNAMES = [ self.manager.getAttributeName( p.values()[0] ) for p in self.ATRIBUTOSLISTA]
            tableColumns = [p.keys()[0] for p in self.ATRIBUTOSLISTA]

        self.tableItems = MyTableWidget(
            self.twItems, tableColumns, self.alignmentColumns, fnParseItem=self.fnParseTableItem)
        # conecta el menu contextual a la tabla
        #self.connect( self.tableItems.widget, QtCore.SIGNAL( 'customContextMenuRequested(const QPoint&)' ), self.on_context_menu )

    def reloadList( self ):
        '''
        Vuelve a cargar la lista a partir de los valores actuales en
        la barra de busqueda y el filtro seleccionado.
        '''
        valor = u''
        campo = u''
        if self.widgets['leSearch']:
            valor = unicode( self.leSearch.text().toUtf8(), 'utf-8' )
        if self.widgets['cbFilters']:
            campo = unicode( self.cbFilters.itemText(
                    self.cbFilters.currentIndex() ).toUtf8() )
        if self.ATRI_COMBO_BUSQUEDA :
            campo = [p[campo] for p in self.ATRI_COMBO_BUSQUEDA if campo in p ][0]
        else:
            campo = self._obtainColumnForName( campo )
        resultado = self.manager.searchBy( campo, valor )
        if self.fnFilterItems:
            resultado = self.fnFilterItems(resultado)
        self.items = resultado
        self.loadTable( resultado )
        if self.widgets['leSearch']:
            self._setSearchColor( self.leSearch, resultado )

    def loadTable( self, listadeobj = None ):
        '''
        Carga la lista de objetos en la tabla
        @param listadeobj:if none carga todos, sino lo de la lista
        '''
        if listadeobj == None:
            listadeobj = self.fnAllItems()
        if self.fnFilterItems:
            listadeobj = self.fnFilterItems(listadeobj)
        self.items = listadeobj
        listadefilas = [self._getAttributesValues( obj ) for obj in listadeobj]
        self.tableItems.addItems( listadefilas )
        self.setItemsCount( len( listadeobj ) )

    def loadCombobox( self ):
        '''
        Carga el combobox de campos
        '''
        if self.widgets['cbFilters']:
            self.cbFilters.clear()
            if not self.ATRI_COMBO_BUSQUEDA :
                atributos = self.manager.getClassAttributes()
                for atributo in atributos:
                    self.ATRI_COMBO_BUSQUEDA.append( {atributo:self._obtainColumnForName( atributo )} )
            map( self.cbFilters.addItem, [p.keys()[0] for p in self.ATRI_COMBO_BUSQUEDA] )

    def find( self ):
        '''
        Reliza la busqueda y carga la tabla
        '''
        # obtiene el valor cargado en la barra de busqueda
        valor = u''
        if self.widgets['leSearch']:
            valor = unicode(self.leSearch.text().toUtf8(),'utf-8')
        # carga la lista segun el estado de la barra de busqueda
        self.reloadList() if valor != u'' else self.loadTable()

    def actualRowsToObjects( self ):
        '''
        Obtiene los objetos seleccionados en la tabla
        @return: un objeto del tipo que maneja self.manager
        '''
        try:
            widget = self.tableItems.widget
            items = widget.selectedItems()
            idxs = list(set([item.row() for item in items]))
            result = [self.items[idx] for idx in idxs]
            return result
        except Exception, e:
            print 'error:actualRowsToObjects:', e
            return None

    def setItemsCount( self, valor ):
        'Set the count items in the label of list'
        if self.widgets['lbItemsCount']:
            self.lbItemsCount.setText( str( valor ) + self.getMsgByLang('itemsCount'))

###############
# API TO VARS #
###############

    def addColumn(self, *args, **kwargs):
        self.addTableColumn(*args, **kwargs)

    def addTableColumn(self, showName, classAttribute, fnParse = None, alignment = 'L'):
        item = {}
        item[showName] = classAttribute
        self.ATRIBUTOSLISTA.append(item)
        if fnParse:
            idx = len(self.ATRIBUTOSLISTA) - 1
            self.fnsParseListAttrs.append([idx, fnParse])

        self.alignmentColumns.append(alignment)

    def addFilter(self, showName, classAttribute):
        item = {}
        item[showName] = classAttribute
        self.ATRI_COMBO_BUSQUEDA.append(item)

    def disableWidgets(self, widgets):
        for w in widgets:
            if w in self.widgets.keys():
                self.widgets[w] = False
            else:
                print 'ERROR:disableWidgets() > "%s" not is a valid widget' % w
                print '> possibles widgets: ', self.widgets.keys()

#################
# AUX FUNCTIONS #
#################

    def _getAttributesValues( self, obj ):
        '''
        Devuelve en una lista los atributos de un objetos, ordenados
        segun lo indicado en self.ATRIBUTOSLISTA
        '''

        resultado = []
        atributos_objeto = self.manager.getClassAttributesValues( obj )
        if not self.ATRIBUTOSLISTA :
            return atributos_objeto
        else:
            atributos_clase = self.manager.getClassAttributes()
            atributos_ordenados = self.ATRIBUTOSLISTA_CLASSNAMES
            for atributo in atributos_ordenados:
                resultado.append( atributos_objeto[ atributos_clase.index( atributo ) ] )
            if self.fnsParseListAttrs:
                for item in self.fnsParseListAttrs:
                    idx = item[0]
                    fn = item[1]
                    resultado[idx] = fn(resultado, resultado[idx])
            return resultado

    def _obtainColumnForName(self, columnname):
        '''
        A partir de un string obtiene la columna de storm
        @param columnname:nombre del atributo en str
        @return:
        '''
        #MAGIC###################
        busqueda = self.manager.CLASS.__dict__[columnname]
        if str( type( busqueda ) ) != "<class 'storm.references.Reference'>" :
            try:
                campo = self.manager.CLASS.__dict__['_storm_columns'][busqueda]
            except:
                print "error: gui.obtainColumnForName()"
                campo = busqueda
        else:
            campo = busqueda
        #END MAGIC###############
        return campo

    def _setSearchColor(self, widget, resultados_busqueda):
        color_rojo = 'background-color: rgb(255, 178, 178);'
        try:
            if self.myStyleSheetBlanco == '' :
                if not widget.styleSheet().isEmpty() :
                    style = widget.styleSheet()
                    self.myStyleSheetBlanco = widget.styleSheet()

                    pos1 = style.indexOf( 'QLineEdit' )
                    pos2 = style.indexOf( '}', pos1 )
                    style = style.replace( pos2, 1, color_rojo + '}' )
                    self.myStyleSheetRojo = style
                else:
                    self.myStyleSheetRojo = color_rojo

            if not widget.text().isEmpty() :
                if len( resultados_busqueda ) == 0 :
                    widget.setStyleSheet( self.myStyleSheetRojo )
                else:
                    widget.setStyleSheet('')
            else:
                widget.setStyleSheet('')
        except:
            self.myStyleSheetBlanco = ''
            self.myStyleSheetRojo = ''
            self._setSearchColor( widget, resultados_busqueda )

    def _get_attributes_names( self ):
        '''
        Obtiene los atributos de la clase que maneja self.manager
        '''
        return self.ATRIBUTOSLISTA_CLASSNAMES if self.ATRIBUTOSLISTA else self.manager.getClassAttributes()

    def on_context_menu( self, point ):
        mypoint = QtCore.QPoint( point.x() + 10, point.y() + 30 )
        self.popMenu = QtGui.QMenu( self )
        self.popMenu.addAction(self.getMsgByLang('new'), self.on_btNew_clicked ,QtGui.QKeySequence("Ctrl+N"))
        self.popMenu.addAction(self.getMsgByLang('edit'), self.on_btEdit_clicked ,QtGui.QKeySequence("Ctrl+M"))
        self.popMenu.addAction(self.getMsgByLang('delete'), self.on_btDelete_clicked ,QtGui.QKeySequence("Del"))

        self.popMenu.exec_(self.tableItems.widget.mapToGlobal(mypoint) )

##########################
# METHODS TO REIMPLEMENT #
##########################

    def add( self ):
        'Call the add dialog window'
        #REIMPLEMENT
        return self.DialogAddClass( self.manager, itemToEdit = False, managers = self.managers, parent=self.parent)

    def edit( self, obj ):
        'Call the edit dialog window'
        #REIMPLEMENT
        return self.DialogAddClass( self.manager, itemToEdit = obj, managers = self.managers, parent=self.parent)

    def delete( self, obj ):
        'Delete a determinated object'
        #REIMPLEMENT
        self.manager.delete( obj )

###################
# EVENT FUNCTIONS #
###################

    def on_leSearch_textChanged( self, cadena ):
        self.find()

    @QtCore.pyqtSlot( int )
    def on_cbFilters_currentIndexChanged ( self, entero ):
        if self.widgets['leSearch']:
            if not self.leSearch.text().isEmpty() :
                self.find()

    @QtCore.pyqtSlot()
    def on_btNew_clicked( self ):
        wAgregar = self.add()
        wAgregar.setWindowIcon(self.windowIcon())
        wAgregar.postSaveMethod = self.reloadList
        wAgregar.exec_()

    @QtCore.pyqtSlot()
    def on_btEdit_clicked( self ):
        listadeobjetosseleccionados = self.actualRowsToObjects()
        if listadeobjetosseleccionados:
            for obj in listadeobjetosseleccionados:
                wEditar = self.edit( obj )
                wEditar.setWindowIcon(self.windowIcon())
                wEditar.postSaveMethod = self.reloadList
                wEditar.exec_()

    @QtCore.pyqtSlot()
    def on_btDelete_clicked( self ):
        listadeobjetosseleccionados = self.actualRowsToObjects()
        if listadeobjetosseleccionados:
            for obj in listadeobjetosseleccionados:
                result = QtGui.QMessageBox.warning(self,
                    self.getMsgByLang('delete'),
                    self.getMsgByLang('deleteConfirm'),
                    QtGui.QMessageBox.Yes, QtGui.QMessageBox.No )
                if result == QtGui.QMessageBox.Yes:
                    self.delete( obj )
                    self.find()

    def on_twItems_itemSelectionChanged(self):
        if self.widgets['btEdit']:
            self.btEdit.setVisible(False)
        if self.widgets['btDelete']:
            self.btDelete.setVisible(False)
        items = self.tableItems.getListSelectedRows()
        if items  :
            if self.widgets['btEdit']:
                self.btEdit.setVisible(True)
            if self.widgets['btDelete']:
                self.btDelete.setVisible(True)
