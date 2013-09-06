import re
import urllib
import gzip
import Queue
from xml.sax import parseString
from xml.sax.handler import ContentHandler
from xml.dom import minidom

records = set(['id', 'value', 'period', 'percent', 'insuranceNumber', 'isVindicated', 'monthlyInstallment', 'type', 'startDate', 'age', 'province', 'condition', 'income', 'expenses', 'credits', 'homeAddressVerificationDescription', 'employerVerificatonDescription', 'identityCardVerificationDescription', 'identityVerificationDescription', 'overdueDays', 'beforeDays', 'maxVerifyMonthlyInstallment', 'positiveRecomendations', 'negativeRecomendations', 'allegroPositiveComments', 'allegroNegativeComments', 'verify'])
keys = Queue.Queue()

def addKey(newKey):
    keys.put(newKey)

def getKey():
    key = keys.get()
    keys.put(key)
    return key

def getValue(singleNode):
    return singleNode.childNodes[0].toxml()

def openURL(url):
    return urllib.urlopen(url)

def getAuctionData(id):
    return minidom.parse(openURL('https://kokos.pl/webapi/get-auction-data?key=' + getKey() + '&id=' + id))

#do poprawy
#def getAuctionsByStatus(status):
#    return minidom.parseString(gzip.open(openURL('https://kokos.pl/webapi/get-auctions-by-status?key=' + getKey() + '&status=' + status), 'rb').read())

def search():
    pass

def getMostPopularAuctions(records):
    return minidom.parse(openURL('https://kokos.pl/webapi/get-most-popular-auctions?key=' + getKey() + '&records=' + str(records)))

def getInvestmentData(ile):
    my_url = "https://kokos.pl/webapi/get-recent-investments?key="+coconutkeys[1]+"&records="+str(ile)
    return minidom.parse(openURL(my_url))

def getRecentPayments(ile):
    my_url = "https://kokos.pl/webapi/get-recent-auctions?key="+coconutkeys[1]+"&records="+str(ile)
    return minidom.parse(openURL(my_url))

def getDataFromAuctionList(idList):
    for id in idList:
        pass


def main():

    #dodaje klucze do kolejki
    addKey('d9cb47b739ee220bc290938262ec602b')
    addKey('9087549eb217b2d43136066a14aa81d4')
    addKey('549a1a7b78dc51ddf8b8c8d585b6ed4b')

    #pobieram skompresowany xml i wypakowuje - dziala
    tempFile = urllib.urlretrieve('https://kokos.pl/webapi/get-auctions-by-status?key=' + getKey() + '&status=500')
    tempGzip = gzip.open(tempFile[0], 'rb')

    handler = ContentHandler()
    xmlsax = parseString(tempGzip.read, handler)
    #parsowanie - dla status=500 nie dziala
    #dom = minidom.parseString(tempGzip.read())
    #print dom.toprettyxml().encode('UTF-8')

    #zapis obiektu dom do xml o nazwie 'dom.xml'
    #file_handle = open('dom.xml','wb')
    #dom.writexml(file_handle)
    #file_handle.close()

    #wydobycie listy aukcji
    auctionsList = dom.childNodes[0].childNodes[0].childNodes

    #operacje na poszczegolnych aukcjach, wypisywanie komunikatu
    #jest problem z komunikatami(opisami) - niektore zawieraja znak nowej linii, co kompletnie psuje zapisany plik, trzeba je pomijac
    for auction in auctionsList:
        dataList = auction.childNodes
        message = ''
        for element in dataList:
            if element.childNodes.length == 1:
                if str(element.nodeName) in records:
                    message = message + element.childNodes[0].toxml().encode('UTF-8') + '*'
            else:
                for personalInfo in element.childNodes:
                    if str(personalInfo.nodeName) in records:
                        data = ''
                        if personalInfo.hasChildNodes():
                            data = personalInfo.childNodes[0].toxml().encode('UTF-8')
                        message = message + data + '*'
        print message


    #for auctions in auctionsList:
    #  auctionList = auctions.childNodes
    #  for auction in auctionList:
    #    fp = open(getValue(auction.getElementsByTagName('id')[0]) + '.xml', 'wb')
    #    auction.writexml(fp)
    #    fp.close()


    #idList = dict()
    #recentAuctions = getAuctionsByStatus('500')
    #auctions = recentAuctions.getElementsByTagName('auction')
    #for auction in auctions:
    #    tempId = getValue(auction.getElementsByTagName('id')[0])
    #    idList[tempId] = getAuctionData(tempId)
    #for auction in idList.keys():
    #    print idList[auction].toprettyxml()




if __name__ == '__main__':
    main()
