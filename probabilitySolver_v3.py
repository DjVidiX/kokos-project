#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      s294063
#
# Created:     24-09-2013
# Copyright:   (c) s294063 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from random import randint
from time import gmtime, strftime
import os

best_solution = []

def saveAuctions(save_table, file_name):
    showValues(save_table)
    my_file = open(file_name, "wb")
    for i in save_table:
        my_file.write(i.name+", ")
        my_file.write(str(i.risk)+", ")
        my_file.write(str(i.income)+", ")
        my_file.write(str(i.value)+"\n")
    my_file.close()

def loadAuctions(file_name):
    work_table = []
    my_file = open(file_name, "r")
    my_string = my_file.read()
    my_table = my_string.split("\n")
    for i in xrange(len(my_table)-1):
        new_tab = my_table[i].split(", ")
        work_table.append(Auction([new_tab[0], float(new_tab[1]), float(new_tab[2])]))
        work_table[i].value = float(new_tab[3])
    return work_table


def ShowTime():
    print strftime("%Y-%m-%d %H:%M:%S", gmtime())

class Auction:
    def __init__(self, args):
        self.name = args[0]
        self.risk = float(args[4])
        self.income = float(args[5])
        self.incrisk = self.income / self.risk
        self.value = float(0)
        self.lose = self.risk-1
        self.win = 1 - self.lose
        self.expected = (self.value)*(self.income*0.01)*self.win - self.value*self.lose

    def Recalculate(self):
        self.expected = (self.value)*(self.income*0.01)*self.win - self.value*self.lose

    def ClearValue(self):
        self.value = float(0)


def clearValues(work_table):
    for i in work_table:
        i.ClearValue()
    return work_table

def showValues(work_table):
    for i in work_table:
        print i.value

def generateInvestment(auction_table, total, pieces, max_val):
    one_piece = total / pieces
    counter = 0
    work_table = auction_table
    while (counter < pieces):
        my_random = randint(0,100) % len(auction_table)
        if (work_table[my_random].value) <= (max_val - one_piece):
            work_table[my_random].value = work_table[my_random].value + one_piece
            counter = counter+1
    return work_table

def calculateRisk(work_table, total):
    risk_total = 0
    for i in work_table:
        risk_total = risk_total + (float(i.value) / float(total))*i.risk
    return risk_total

def calculateIncome(work_table, total):
    inc_total = 0
    for i in work_table:
        inc_total = inc_total + (float(i.value) / float(total))*i.income
    return inc_total

def calculateExpected(work_table):
    exp_total = 0
    for i in work_table:
        i.Recalculate()
        exp_total = exp_total + i.expected
    return exp_total

def probabilityRiskSolver(auction_table, total, pieces, max_val, tries):
    current_risk = 2
    for i in xrange(tries):
        work_table = auction_table
        generateInvestment(work_table, total, pieces, max_val)
        calculated = calculateRisk(work_table, total)
        if calculated < current_risk:
            best_solution = []
            best_solution.extend(work_table)
            saveAuctions(best_solution, "solution.txt")
            current_risk = calculated
            print current_risk
        clearValues(work_table)


def probabilityIncomeSolver(auction_table, total, pieces, max_val, tries):
    current_income = 0
    for i in xrange(tries):
        work_table = auction_table
        generateInvestment(work_table, total, pieces, max_val)
        calculated = calculateIncome(work_table, total)
        if calculated > current_income:
            best_solution = []
            best_solution.extend(work_table)
            saveAuctions(best_solution, "solution.txt")
            current_income = calculated
            print current_income

        clearValues(work_table)

def probabilityExpectedSolver(auction_table, total, pieces, max_val, tries):
    current_expected = -1000
    for i in xrange(tries):
        work_table = auction_table
        generateInvestment(work_table, total, pieces, max_val)
        calculated = calculateExpected(work_table)
        if calculated > current_expected:
                best_solution = []
                best_solution.extend(work_table)
                current_expected = calculated
                print current_expected
                saveAuctions(best_solution, "solution.txt")
        clearValues(work_table)


"""
auction_table = []
total =1000

auction_table.append(Auction("aukcja1", 6, 1))
auction_table.append(Auction("aukcja2", 1, 1))
auction_table.append(Auction("aukcja3", 9.6, 1.02))
auction_table.append(Auction("aukcja4", 16, 1.03))
auction_table.append(Auction("aukcja5", 16, 1.04))
auction_table.append(Auction("aukcja6", 16, 1.05))
auction_table.append(Auction("aukcja7", 16, 1.054))
auction_table.append(Auction("aukcja8", 16, 1.056))
auction_table.append(Auction("aukcja9", 10, 1.059))
auction_table.append(Auction("aukcja10", 16, 1.06))
auction_table.append(Auction("aukcja11", 16, 1.067))
auction_table.append(Auction("aukcja12", 16, 1.075))
auction_table.append(Auction("aukcja13", 16, 1.076))
auction_table.append(Auction("aukcja14", 8, 1.087))
auction_table.append(Auction("aukcja15", 16, 1.093))
auction_table.append(Auction("aukcja16", 16, 1.093))
auction_table.append(Auction("aukcja17", 16, 1.095))
auction_table.append(Auction("aukcja18", 16, 1.096))
auction_table.append(Auction("aukcja19", 16, 1.1))
auction_table.append(Auction("aukcja20", 10, 1.106))

#showValues(auction_table)
#showValues(generateInvestment(auction_table, 1000, 10, 300))
#showValues(clearValues(auction_table))

ShowTime()

#expected_risk = probabilityRiskSolver(auction_table, total, 20, 50, 10000)
#expected_income = probabilityIncomeSolver(auction_table, total, 20, 300, 10000)

#expected_solution = probabilityExpectedSolver(auction_table, total, 20, 200, 10000)

showValues(loadAuctions("solution.txt"))

ShowTime()
"""

