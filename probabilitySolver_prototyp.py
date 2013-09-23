#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      s294063
#
# Created:     23-09-2013
# Copyright:   (c) s294063 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from random import randint
from time import gmtime, strftime
import os

def ShowTime():
    print strftime("%Y-%m-%d %H:%M:%S", gmtime())

auction_table = []

class Auction:
    def __init__(self, name, income, risk):
        self.name = name
        self.risk = float(risk)
        self.income = float(income)
        self.incrisk = income / risk
        self.value = float(0)
        self.lose = self.risk-1
        self.win = 1 - self.lose
        self.expected = (self.value)*(self.income*0.01)*self.win - self.value*self.lose

    def Recalculate(self):
        self.expected = (self.value)*(self.income*0.01)*self.win - self.value*self.lose

    def ClearValue(self):
        self.value = float(0)

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
    return exp_total\

def clearValues(work_table):
    new_table = []
    for i in work_table:
        new_table.append(i.ClearValue())
    return new_table

def probabilitySolver(auction_table, total, pieces, max_val, tries, mode):
    best_solve = []
    current_risk = 2
    if mode == "risk":
        for i in xrange(tries):

            work_table = []
#            work_table.append(auction_table) tu co sie sypie przy przekazywaniu listy


            new_table = generateInvestment(work_table, total, pieces, max_val)
            calculated = calculateRisk(new_table, total)
            print calculated
            if calculated < current_risk:
                best_solve = new_table
                current_risk = calculated
                print current_risk
                ShowTime()
    return current_risk


  #  if mode == "income":
  #  if mode == "expected":



auction_table.append(Auction("aukcja1", 16, 1.1))
auction_table.append(Auction("aukcja2", 16, 1.15))
auction_table.append(Auction("aukcja3", 15, 1.05))
auction_table.append(Auction("aukcja4", 14, 1.08))
auction_table.append(Auction("aukcja5", 13, 1.12))

total = 1000

print probabilitySolver(auction_table, total, 10, 500, 5, "risk")

