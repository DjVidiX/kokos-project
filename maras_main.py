import re
import urllib
import gzip
import Queue
from parser import JAMParser
from xml.sax import parseString
from xml.sax.handler import ContentHandler
from xml.dom import minidom

records = ['id', 'value', 'period', 'percent', 'insuranceNumber', 'isVindicated', 'monthlyInstallment', 'type', 'startDate', 'age', 'province', 'condition', 'income', 'expenses', 'credits', 'homeAddressVerificationDescription', 'employerVerificationDescription', 'identityCardVerificationDescription', 'identityVerificationDescription', 'overdueDays', 'beforeDays', 'maxVerifyMonthlyInstallment', 'positiveRecomendations', 'negativeRecomendations']
keys = Queue.Queue()

def addKey(newKey):
    keys.put(newKey)

def getKey():
    key = keys.get()
    keys.put(key)
    return key

def parse1300(ms_str):
    Parser = JAMParser()
    auctions = []
    for aukcja in ms_str:
        aukcja = aukcja.replace('&lt;![CDATA[','').replace(']]&gt;', '').replace('&amp;oacute;', 'o')
        for klucz in records:
            war = Parser.getData(klucz, aukcja)
            if(war):
                if(klucz=='id'):
                    if(len(auctions)>0):
                        if(len(auctions[len(auctions)-1]) == 1):
                            auctions.pop()
                    auctions.append([war])
                else:
                    auctions[len(auctions)-1].append(war)
        if(len(auctions[len(auctions)-1]) != len(records)):
            auctions.pop()
        else:
            ver = Parser.getVerify(aukcja)
            auctions[len(auctions)-1].append(ver)
            rem = Parser.reminderDla1300(aukcja)
            if(rem):
                auctions[len(auctions)-1].append(rem) 
    return auctions
    
def parse500(ms_str):
    Parser = JAMParser()
    auctions = []
    for aukcja in ms_str:
        aukcja = aukcja.replace('&lt;![CDATA[','').replace(']]&gt;', '').replace('&amp;oacute;', 'o')
        rem = Parser.reminderDla500(aukcja)
        if(rem):
            ver = Parser.getVerify(aukcja)
            for klucz in records:
                war = Parser.getData(klucz, aukcja)
                if(war):
                    if(klucz=='id'):
                        if(len(auctions)>0):
                            if(len(auctions[len(auctions)-1]) <= 2):
                                auctions.pop()
                        auctions.append([war])
                    else:
                        auctions[len(auctions)-1].append(war)
            auctions[len(auctions)-1].append(ver)
            auctions[len(auctions)-1].append(rem) 
    return auctions

def main():

    #dodaje klucze do kolejki
    addKey('d9cb47b739ee220bc290938262ec602b')
    addKey('9087549eb217b2d43136066a14aa81d4')
    addKey('549a1a7b78dc51ddf8b8c8d585b6ed4b')

    #pobieram skompresowany xml i wypakowuje - dziala
    tempFile = urllib.urlretrieve('https://kokos.pl/webapi/get-auctions-by-status?key=' + getKey() + '&status=1300')
    
    tempGzip = gzip.open(tempFile[0], 'rb')
    
    ms_str = tempGzip.read()
    ms_str = ms_str.split("</auction>")
    
    #auctions = parse500()
    auctions = parse1300(ms_str)
    
    plik = open('dane_1300.txt', 'wb')
    
    maras = 'id*value*period*percent*insuranceNumber*isVindicated*monthlyInstallment*type*startDate*age*province*condition*income*expenses*credits*homeAddressVerificationDescription*employerVerificationDescription*identityCardVerificationDescription*identityVerificationDescription*overdueDays*beforeDays*maxVerifyMonthlyInstallment*positiveRecomendations*negativeRecomendations*verify*reminder*\n'
    
    for aukcja in auctions:
        for string in aukcja:
            maras = maras  + string + '*'
        maras = maras + '\n'
    
    plik.write(maras)
    plik.close()

if __name__ == '__main__':
    main()
