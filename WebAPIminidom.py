#import re
#import gzip
import urllib
import Queue
from xml.dom import minidom

class WebAPI:

    def __init__(self):
        self.keys = Queue.Queue()

    def __del__(self):
        del self

    def addKey(self, newKey):
        self.keys.put(newKey)

    def getKey(self):
        key = self.keys.get()
        self.keys.put(key)
        return key

    def openURL(self, url):
        return urllib.urlopen(url)

    def getAuctionData(self, id):
        return minidom.parse(openURL('https://kokos.pl/webapi/get-auction-data?key=' + self.getKey() + '&id=' + str(id)))

    def search(self,
        status = None,
        userId = None,
        valueFrom = None,
        valueTo = None,
        periodFrom = None,
        periodTo = None,
        percentFrom = None,
        percentTo = None
        ):
        return minidom.parse(openURL('https://kokos.pl/webapi/search?' +
        (userId and 'user_id=' + str(userId) + '&'  or '' ) +
        (valueFrom and 'valueFrom=' + str(valueFrom) + '&'  or '' ) +
        (valueTo and 'valueTo=' + str(valueTo) + '&'  or '' ) +
        (periodFrom and 'periodFrom=' + str(periodFrom) + '&'  or '' ) +
        (periodTo and 'periodTo=' + str(periodTo) + '&'  or '' ) +
        (percentFrom and 'percentFrom=' + str(percentFrom) + '&'  or '' ) +
        (percentTo and 'percentTo=' + str(percentTo) + '&'  or '' ) +
        (status and 'status=' + str(status) + '&' or '' ) + 'key=' + self.getKey()))

    def getMostPopularAuctions(self, records):
        return minidom.parse(openURL('https://kokos.pl/webapi/get-most-popular-auctions?key=' + self.getKey() + '&records=' + str(records)))

    def getRecentInvestments(self, records):
        return minidom.parse(openURL("https://kokos.pl/webapi/get-recent-investments?key=" + self.getKey() + "&records=" + str(records)))

    def getRecentAuctions(self, records):
        return minidom.parse(openURL("https://kokos.pl/webapi/get-recent-auctions?key=" + self.getKey() + "&records=" + str(records)))

'''
def main():
    #dodaje klucze do kolejki
    addKey('d9cb47b739ee220bc290938262ec602b')
    addKey('9087549eb217b2d43136066a14aa81d4')
    addKey('549a1a7b78dc51ddf8b8c8d585b6ed4b')

    dom = search(valueFrom = 1100, status = 100)
    print dom.toprettyxml().encode('UTF-8')

    #Pobranie i wypakowanie pliku .xml
    tempFile = urllib.urlretrieve('https://kokos.pl/webapi/get-auctions-by-status?key=' + getKey() + '&status=110')
    tempGzip = gzip.open(tempFile[0], 'rb')
    dom = minidom.parseString(tempGzip.read())
    #print dom.toprettyxml().encode('UTF-8')

    #Operacje na poszczegolnych aukcjach, wypisywanie komunikatu
    for i in range(30711,30712 - 3300, -1):
        print i
        dataList = getAuctionData(idList[i]).childNodes[0].childNodes[0].childNodes
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
                        message = message +  data + '*'
            message = message.replace('<![CDATA[', '').replace(']]', '').replace('>', '') + '\n'

if __name__ == '__main__':
    main()
'''