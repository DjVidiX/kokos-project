import re
import urllib
import gzip
from xml.dom import minidom

coconutkeys = ["d9cb47b739ee220bc290938262ec602b","549a1a7b78dc51ddf8b8c8d585b6ed4b" ]


def getValue(singleNode):
    return singleNode.childNodes[0].toxml()

def decompressFile(file, parameter):
    return minidom.parseString(gzip.open(file, parameter))

def openURL(url):
    return urllib.urlopen(url)


def getInvestmentData(ile):
    my_url = "https://kokos.pl/webapi/get-recent-investments?key="+coconutkeys[1]+"&records="+str(ile)
    return minidom.parse(openURL(my_url))

def getRecentPayments(ile):
    my_url = "https://kokos.pl/webapi/get-recent-auctions?key="+coconutkeys[1]+"&records="+str(ile)
    return minidom.parse(openURL(my_url))

for i in range(0,15):
    getInvestmentData(1)
    print(i)
