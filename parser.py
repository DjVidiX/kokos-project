import re
import urllib
import gzip
import Queue
from parser import JAMParser
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
    tempFile = urllib.urlretrieve('https://kokos.pl/webapi/get-auctions-by-status?key=' + getKey() + '&status=1300')
    
    tempGzip = gzip.open(tempFile[0], 'rb')

    Parser = JAMParser()
    
    Parser.feed(tempGzip.read())
    id_list = Parser.getData()
    
    print id_list[32600:]
    #print len(id_list) 
    
    """for lista in id_list:
        for dana in lista:
            if(re.search("<verify>.*</verify>", dana)):
                print 'YeaH ! ' """
    
    
    #handler = ContentHandler()
    #xmlsax = parseString(tempGzip.read, handler)
    #parsowanie - dla status=500 nie dziala
    #dom = minidom.parseString(tempGzip.read())
    #print dom.toprettyxml().encode('UTF-8')

    #zapis obiektu dom do xml o nazwie 'dom.xml'
    #file_handle = open('dom.xml','wb')
    #dom.writexml(file_handle)
    #file_handle.close()

    #wydobycie listy aukcji
    """auctionsList = dom.childNodes[0].childNodes[0].childNodes

    #operacje na poszczegolnych aukcjach, wypisywanie komunikatu
    #jest problem z komunikatami(opisami) - niektore zawieraja znak nowej linii, co kompletnie psuje zapisany plik, trzeba je pomijac
    my_own_file = open('dane.txt', 'wb')
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

        string_to_save = message.replace('<![CDATA[', '').replace(']]', '').replace('>', '')
        my_own_file.write(string_to_save)
    """

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
tion name="geany" exec="&apos;geany %u&apos;" modified="2013-09-06T12:39:19Z" count="1"/>
        </bookmark:applications>
      </metadata>
    </info>
  </bookmark>
  <bookmark href="file:///home/students/s375261/Desktop/PPB/kokos-project/dane.txt" added="2013-09-06T13:21:10Z" modified="2013-09-06T13:45:40Z" visited="2013-09-06T13:21:10Z">
    <info>
      <metadata owner="http://freedesktop.org">
        <mime:mime-type type="text/plain"/>
        <bookmark:groups>
          <bookmark:group>pluma</bookmark:group>
        </bookmark:groups>
        <bookmark:applications>
          <bookmark:application name="File Manager" exec="&apos;pluma %U&apos;" modified="2013-09-06T13:45:29Z" count="5"/>
          <bookmark:application name="Pluma" exec="&apos;pluma %u&apos;" modified="2013-09-06T13:45:40Z" count="5"/>
        </bookmark:applications>
      </metadata>
    </info>
  </bookmark>
  <bookmark href="file:///home/students/s375261/Downloads/LM1%20(1).pdf" added="2013-09-09T11:30:58Z" modified="2013-09-09T11:30:58Z" visited="2013-09-09T11:30:58Z">
    <info>
      <metadata owner="http://freedesktop.org">
        <mime:mime-type type="application/pdf"/>
        <bookmark:applications>
          <bookmark:application name="Document Viewer" exec="&apos;atril %u&apos;" modified="2013-09-09T11:30:58Z" count="1"/>
        </bookmark:applications>
      </metadata>
    </info>
  </bookmark>
  <bookmark href="file:///home/students/s375261/Downloads/getAuctionByStatus_1300.xml%20(1).bz" added="2013-09-09T11:46:31Z" modified="2013-09-09T11:46:31Z" visited="2013-09-09T11:46:31Z">
    <info>
      <metadata owner="http://freedesktop.org">
        <mime:mime-type type="application/x-bzip"/>
        <bookmark:applications>
          <bookmark:application name="Engrampa" exec="&apos;engrampa&apos;" modified="2013-09-09T11:46:31Z" count="3"/>
        </bookmark:applications>
      </metadata>
    </info>
  </bookmark>
  <bookmark href="file:///home/students/s375261/Desktop/PPB/parser.py" added="2013-09-09T11:54:22Z" modified="2013-09-09T13:21:53Z" visited="2013-09-09T11:54:23Z">
    <info>
      <metadata owner="http://freedesktop.org">
        <mime:mime-type type="text/x-python"/>
        <bookmark:groups>
          <bookmark:group>pluma</bookmark:group>
        </bookmark:groups>
        <bookmark:applications>
          <bookmark:application name="geany" exec="&apos;geany %u&apos;" modified="2013-09-09T11:54:23Z" count="2"/>
          <bookmark:application name="File Manager" exec="&apos;geany %F&apos;" modified="2013-09-09T13:21:53Z" count="2"/>
          <bookmark:application name="Pluma" exec="&apos;pluma %u&apos;" modified="2013-09-09T13:21:50Z" count="2"/>
        </bookmark:applications>
      </metadata>
    </info>
  </bookmark>
  <bookmark href="file:///home/students/s375261/Desktop/PPB/temp.xml" added="2013-09-09T12:13:04Z" modified="2013-09-09T12:13:04Z" visited="2013-09-09T12:13:04Z">
    <info>
      <metadata owner="http://freedesktop.org">
        <mime:mime-type type="application/xml"/>
        <bookmark:applications>
          <bookmark:application name="geany" exec="&apos;geany %u&apos;" modified="2013-09-09T12:13:04Z" count="2"/>
        </bookmark:applications>
      </metadata>
    </info>
  </bookmark>
  <bookmark href="file:///home/students/s375261/Desktop/PPB/kokos-project/main.py" added="2013-09-09T12:17:36Z" modified="201