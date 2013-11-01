#!/usr/bin/env python

from random import randint
from time import gmtime, strftime
import os

def ShowTime():
    print strftime("%Y-%m-%d %H:%M:%S", gmtime())

def saveAuctions(save_table, file_name):
    my_file = open(file_name, "wb")
    for i in save_table:
        my_file.write(i.name.replace("\n", "")+", ")
        my_file.write(str(i.risk)+", ")
        my_file.write(str(i.income)+", ")
        my_file.write(str(i.value)+"\n")
    my_file.close()

def loadAuctions(file_name):
    work_table = []
    my_file = open(file_name, "r")
    my_table = my_file.readlines()
    for line in my_table:
        dane = line.split(", ")
        work_table.append(dane[3])
    return work_table

class Auction:
    def __init__(self, args):
        self.name = args[0]
        self.risk = float(args[2])
        self.income = float(args[1]*0.01)
        self.value = float(0)
        self.lose = self.risk-1
        self.win = 1 - self.lose
        self.expected = (self.value)*(self.income)*self.win - self.value*self.lose

    def Recalculate(self):
        self.expected = (self.value)*(self.income)*self.win - self.value*self.lose

    def ClearValue(self):
        self.value = float(0)

    def getDescription(self):
        my_string = self.name + ", " + str(self.income) + ", " + str(self.risk) + ", " + str(self.value)+ "\n"
        return my_string

    def setValue(self, val):
        self.value = float(val)

def clearValues(work_table):
    for i in work_table:
        i.ClearValue()
    return work_table

def showValues(work_table):
    for i in work_table:
        print i.value

def getValues(work_table): #argument to tablica odczytana z pliku, zwraca tablic? intow
    new_table = []
    for i in work_table:
        new_table.append(float(i.replace("\n", "")))
    return new_table

def generateInvestment(auction_table, total, pieces, max_val):
    #print total, pieces
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
        inc_total = inc_total + (float(i.value))*i.income
    return inc_total

def calculateExpected(work_table):
    exp_total = 0
    for i in work_table:
        i.Recalculate()
        exp_total = exp_total + i.expected
    return exp_total

def printAllCalculated(work_table, total):
    summary = "Expected = "
    summary+= str(calculateExpected(work_table))
    summary+= ", Income = "
    summary+= str(calculateIncome(work_table, total))
    summary+= ", Risk = "
    summary+= str(calculateRisk(work_table, total))
    print summary

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
            #print current_risk
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
                saveAuctions(best_solution, "solution.txt")
        clearValues(work_table)

def generateAuction(): # generuje pojedyncze losowe aukcje
    name="auction"
    my_random = randint(0,1000) %1000
    name+=str(my_random)
    income = 8 + my_random %9
    risk = 1 + (my_random %200)*0.001
    argtable = [name, income, risk]
    auction = Auction(argtable)
    return auction

def generateAuctionList(x): # generuje list? x losowych aukcji do testow
    auction_table = []
    for i in range(0, x):
        auction_table.append(generateAuction())
    return auction_table

def printAuctionList(auction_table): # wypisuje liste aukcji i ch parametry (zeby sprawdzac ich poprawnosc)
    my_string =""
    for i in auction_table:
        my_string+=i.getDescription()
    print my_string

def rebindValues(auction_table, values_table): # laczy liste aukcji z wartosciami wczytanymi z pliku
    k = len(auction_table)

    for i in range (0, k):
       auction_table[i].setValue(values_table[i])
    return auction_table

def getInvestedTotal(auction_table): # liczy ile faktycznie zostalo zainwestowane w aukcje z listy
    total = 0
    for i in auction_table:
        total+=i.value
    return total

def SimulateIncome(x):
    ShowTime()
    auction_table = generateAuctionList(x)
    my_total = 1000 + (randint(0, 100)%8)*1000
    my_max = my_total*0.2
    my_piece = my_total *0.02
    expected_income = probabilityIncomeSolver(auction_table, my_total, my_piece, my_max, 10000)
    auction_table = rebindValues(auction_table, getValues(loadAuctions("solution.txt")))
    printAuctionList(auction_table)
    print getInvestedTotal(auction_table)
    printAllCalculated(auction_table, my_total)
    ShowTime()

def SimulateRisk(x):
    ShowTime()
    auction_table = generateAuctionList(x)
    my_total = 1000 + (randint(0, 100)%8)*1000
    my_max = my_total*0.2
    my_piece = my_total *0.02
    expected_risk = probabilityRiskSolver(auction_table, my_total, my_piece, my_max, 10000)
    auction_table = rebindValues(auction_table, getValues(loadAuctions("solution.txt")))
    printAuctionList(auction_table)
    print getInvestedTotal(auction_table)
    printAllCalculated(auction_table, my_total)
    ShowTime()

def SimulateExpected(x):
    ShowTime()
    auction_table = generateAuctionList(x)
    my_total = 1000 + (randint(0, 100)%8)*1000
    my_max = my_total*0.2
    my_piece = my_total *0.02
    expected_solution = probabilityExpectedSolver(auction_table, my_total, my_piece, my_max, 10000)
    auction_table = rebindValues(auction_table, getValues(loadAuctions("solution.txt")))
    printAuctionList(auction_table)
    print getInvestedTotal(auction_table)
    printAllCalculated(auction_table, my_total)
    ShowTime()

def SimulateEverything(x):
    ShowTime()
    auction_table = generateAuctionList(x)
    my_total = 1000 + (randint(0, 100)%8)*1000
    my_max = my_total*0.2
    my_piece = my_total *0.02

    expected_solution = probabilityExpectedSolver(auction_table, my_total, my_piece, my_max, 10000)

    auction_table = rebindValues(auction_table, getValues(loadAuctions("solution.txt")))
    printAuctionList(auction_table)
    print getInvestedTotal(auction_table)
    printAllCalculated(auction_table, my_total)
    clearValues(auction_table)
    ShowTime()

    expected_income = probabilityIncomeSolver(auction_table, my_total, my_piece, my_max, 10000)
    auction_table = rebindValues(auction_table, getValues(loadAuctions("solution.txt")))
    printAuctionList(auction_table)
    print getInvestedTotal(auction_table)
    printAllCalculated(auction_table, my_total)
    clearValues(auction_table)
    ShowTime()

    expected_risk = probabilityRiskSolver(auction_table, my_total, my_piece, my_max, 10000)
    auction_table = rebindValues(auction_table, getValues(loadAuctions("solution.txt")))
    printAuctionList(auction_table)
    print getInvestedTotal(auction_table)
    printAllCalculated(auction_table, my_total)
    clearValues(auction_table)
    ShowTime()

best_solution = []

x = 20 # x to zmienna oznaczajca liczbe aukcji, dla ktorych ma zostac odpalona symulacja

#SimulateExpected(x)

#SimulateIncome(x)

#SimulateRisk(x)

SimulateEverything(x)