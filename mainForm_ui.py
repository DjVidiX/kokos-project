# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainForm.ui'
#
# Created: Mon Sep 16 15:56:44 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(655, 345)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(11, 11, 628, 286))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.widget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.TableView = QtGui.QTableView(self.widget)
        self.TableView.setObjectName(_fromUtf8("TableView"))
        self.gridLayout_2.addWidget(self.TableView, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_4.addWidget(self.label)
        self.ValueBox = QtGui.QSpinBox(self.widget)
        self.ValueBox.setMinimum(50)
        self.ValueBox.setMaximum(1000000)
        self.ValueBox.setSingleStep(50)
        self.ValueBox.setObjectName(_fromUtf8("ValueBox"))
        self.verticalLayout_4.addWidget(self.ValueBox)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.MonthNumberBox = QtGui.QSpinBox(self.widget)
        self.MonthNumberBox.setMinimum(1)
        self.MonthNumberBox.setMaximum(48)
        self.MonthNumberBox.setObjectName(_fromUtf8("MonthNumberBox"))
        self.verticalLayout_2.addWidget(self.MonthNumberBox)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.GainButton = QtGui.QRadioButton(self.widget)
        self.GainButton.setChecked(True)
        self.GainButton.setObjectName(_fromUtf8("GainButton"))
        self.verticalLayout_3.addWidget(self.GainButton)
        self.RiskButton = QtGui.QRadioButton(self.widget)
        self.RiskButton.setObjectName(_fromUtf8("RiskButton"))
        self.verticalLayout_3.addWidget(self.RiskButton)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setEnabled(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_5.addWidget(self.label_4)
        self.GainRiskBox = QtGui.QSpinBox(self.widget)
        self.GainRiskBox.setEnabled(False)
        self.GainRiskBox.setObjectName(_fromUtf8("GainRiskBox"))
        self.verticalLayout_5.addWidget(self.GainRiskBox)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 2, 2, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 0, 5, 1)
        self.SearchButton = QtGui.QPushButton(self.widget)
        self.SearchButton.setObjectName(_fromUtf8("SearchButton"))
        self.gridLayout.addWidget(self.SearchButton, 1, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 655, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Ile chcesz zainwestować?", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Max. liczba miesięcy?", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Określasz ryzyko czy zysk?", None, QtGui.QApplication.UnicodeUTF8))
        self.GainButton.setText(QtGui.QApplication.translate("MainWindow", "Zysk", None, QtGui.QApplication.UnicodeUTF8))
        self.RiskButton.setText(QtGui.QApplication.translate("MainWindow", "Ryzyko", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Zysk", None, QtGui.QApplication.UnicodeUTF8))
        self.SearchButton.setText(QtGui.QApplication.translate("MainWindow", "Szukaj", None, QtGui.QApplication.UnicodeUTF8))

