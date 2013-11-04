# -*- coding: UTF-8 -*-

import sys
import operator
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from mainForm_ui import Ui_MainWindow
from mytablemodel import MyTableModel
from webapiminidom import WebAPI
import probabilitySolver as solver

class MyForm(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.MyWebAPI = WebAPI()
        self.klucz = self.keyCheck()
        if(self.klucz):
            self.MyWebAPI.addKey(str(self.klucz))
        self.ui.SearchButton.clicked.connect(self.search)
        
        self.statusBar()
        
    def keyCheck(self):
        try:
            plik = open('klucz.txt', 'r')
            klucz = plik.read()
            self.ui.KeyBox.setText(klucz)
            plik.close()
        except IOError:
            klucz = None
        return klucz
        
    def search(self):
        sender = self.sender()
        if not(self.klucz):
            plik = open('klucz.txt', 'w')
            self.klucz = self.ui.KeyBox.text()
            self.MyWebAPI.addKey(str(self.klucz))
            plik.write(self.klucz)
            plik.close()
        value = self.ui.ValueBox.value()
        month_dur = self.ui.MonthNumberBox.value()
        zysk = self.ui.GainBox.value()
        ryzyko = self.ui.RiskBox.value()
        my_array = self.MyWebAPI.getCurrentAuctions('id', 'value', 'percent', 'period', 'totalIncome', value=value, duration=month_dur, risk=ryzyko)
        final_array = []
        if not my_array:
            QMessageBox.about(self, "Puste wyszukiwanie", u"Twoje zapytanie nie zwróciło żadnych wyników")
        else:
            temp_auction = []
            for aukcja in my_array:
                temp_auction.append(solver.Auction(aukcja))
            solver.probabilityRiskSolver(temp_auction, value, value/50, value, 10000)
            income_solution = solver.loadAuctions('solution.txt')
            m_a = []
            i = -1
            for row in my_array:
                i = i+1
                row[1] = income_solution[i]
                if row[1] != 0:
                    row[4] = float((row[1]*row[2])/100) # kwota inwestycji * oprocentowanie aukcji
            for row in my_array:
                if row[1] != 0:
                    row[2] = float(row[2] * 12 / row[3]) # wyznaczam oprocentowanie roczne do wyswietlenia
                    final_array.append(row)
        tablemodel = MyTableModel(final_array, self)
        self.ui.TableView.setModel(tablemodel)
        self.ui.TableView.setSortingEnabled(True)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
