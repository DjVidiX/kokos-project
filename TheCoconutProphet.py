#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      s294063
#
# Created:     16-09-2013
# Copyright:   (c) s294063 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from random import randint
#from PyQt4 import QtGui

#QtCore.QObject.connect(a, QtCore.SIGNAL("QtSig()"), pyFunction) - przyklad wiazania przycisku z funkcja

class Auction:
    dict = {}
    def __init__(self, my_list):
        # tutaj aukcja dostaje parametry z listy
        # po ktorych potem bedziemy wykonywac sortowania i sprawdzanie warunkow
        pass
    def __del__(self):
        del self

def FileExists(filename):
    try:
        with open('filename'): pass
    except IOError:
        print 'Shiiiiiiieeeeeeeeeeeeeeeeeeeet'

def GetData():
    # funkcja ktora zwraca list? aukcji spelniajacej okreslony warunek tzn. status = 100
    # zakoadamy ze zna lokalkizacje klucza
    pass

def AddRisk(my_list):
    for i in my_list:
        my_risk = randint(0, 100)
        i.append(my_risk*0.01)
    # dostaje list?, liczy dla kazdej aukcji jej ryzyko i dodaje jako ostatni parametr
    # tutaj algorytm od matematykow wyliczajacy ryzyko
    return my_list

def SortBy(worklist, parametr):
    # sortowanie obiektow typu Auction po parametrze podanym jako string
    return sorted_list

def CommitList(my_list):
    # wyswietla liste w ekranie tabeli - jakos
    pass

def Search():
    FileExists("key.txt")
    maras = GetData()
    marisk = AddRisk(maras)
    marwork = []
    for i in marisk:
        marwork.append(workauct =Auction(i))
    worklist = []
    for i in marwork:
        if ((i.month <= MonthBox.GetValue() and i.risk <= GainRiskBox.GetValue()) or (i.month<=MonthBox.GetValue() and i.profit <= GainRiskBox.GetValue())):
            worklist.append(i)
    newlist = SortBy(worklist, "risk") # tutaj moze posortowac po risk albo po profit w zaleznosci od tego co zostalo wybrane
    CommitData(newlist)

# search podpiac pod klawisz

list = [[5, 6, 7], [8, 9, 11], [6, 7, 8], [5, 4, 3]]

print AddRisk(list)





