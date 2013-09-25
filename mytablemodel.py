# -*- coding: UTF-8 -*-

import operator
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class MyTableModel(QAbstractTableModel):
    header_labels = ['ID', u'Kwota Inwestycji', 'Oprocentowanie [%]', u'Liczba miesięcy', 'Zysk z odsetek', 'Ryzyko [%]', 'URL']

    def __init__(self, datain, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.arraydata = datain

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.header_labels[section]
        return QAbstractTableModel.headerData(self, section, orientation, role)

    def rowCount(self, parent):
        try:
            return len(self.arraydata)
        except IndexError:
            return 0

    def columnCount(self, parent):
        try:
            return len(self.arraydata[0])
        except IndexError:
            return 0

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(self.arraydata[index.row()][index.column()])

    def sort(self, Ncol, order):
        #Sort table by given column number.
        
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.arraydata = sorted(self.arraydata, key=operator.itemgetter(Ncol))
        if order == Qt.DescendingOrder:
            self.arraydata.reverse()
        self.emit(SIGNAL("layoutChanged()"))
