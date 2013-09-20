import sys
import operator
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from mainForm_ui import Ui_MainWindow
from mytablemodel import MyTableModel
from webapiminidom import WebAPI

class MyForm(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.ui.styleSheet("QLabel {font-size : 400px; color : blue; background-image: url('tmp/test.jpg');}")
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
        #MyWebAPI.addKey(str(klucz))
        my_array = self.MyWebAPI.getCurrentAuctions('value', 'percent', value=value, duration=month_dur, income=zysk, risk=ryzyko)
        tablemodel = MyTableModel(my_array, self)
        self.ui.TableView.setModel(tablemodel)
        self.ui.TableView.setSortingEnabled(True)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
