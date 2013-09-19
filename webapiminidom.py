# -*- coding: UTF-8 -*-

import gzip
import urllib
import Queue
from jamparser import JAMParser
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
		print url
		return urllib.urlopen(url)
	
	def retrieveURL(self, url):
		print url
		return urllib.urlretrieve(url)[0]
	
	def getValue(self, singleNode):
		return str(singleNode.childNodes[0].toxml().encode('UTF-8')).replace('<![CDATA[', '').replace(']]', '').replace('>', '')

	def getAuctionData(self, id):
		return minidom.parse(self.openURL('https://kokos.pl/webapi/get-auction-data?key=' + self.getKey() + '&id=' + str(id)))
		
	def getAuctionsByStatus(self, status):
		tempFile = self.retrieveURL('https://kokos.pl/webapi/get-auctions-by-status?key=' + self.getKey() + '&status=' + str(status))
		return minidom.parseString(gzip.open(tempFile, 'rb').read()).childNodes[0].childNodes[0].childNodes
		
	def getCurrentAuctionsByRisk(self):
		riskParameters = {}
		auctions = []
		tempAuction = {}
		currentAuctions = self.getAuctionsByStatus(100)
		for auction in currentAuctions:
			for element in auction.childNodes:
				if str(element.nodeName) in riskParameters:
					tempAuction[str(element.nodeName)] = self.getValue(element)
			tempAuction['risk'] = 0 #TUTAJ POTRZEBNY JEST WZÓR NA WYZNACZENIE RYZYKA DLA DANEJ AUKCJI
			tempAuction['url'] = ('https://kokos.pl/aukcje?id=' + self.getValue(auction.getElementsByTagName('id')[0]))
			auctions.append(tempAuction)
			tempAuction = {}
		return auctions
	
	def getCurrentAuctions(self, *records, **inputValues):
		auctions = []
		currentAuctions = self.getCurrentAuctionsByRisk()
		for auction in currentAuctions:
			if (float(inputValues['value']) * float(auction['percent']) >= float(inputValues['income'])) and (auction['risk'] <= inputValues['risk']) and (int(auction['period']) <= inputValues['duration']):
				 auctions.append(auction)
		return [for auction in auctions self.convertDictionaryToList(auction, records.append('risk').append('url')]
		
	def convertDictionaryToList(self, dicAuction, records):
		listAuction = []
		for record in records:
			tempList.append(dicAuction[record])
		return listAuction
	
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
		return minidom.parse(self.openURL('https://kokos.pl/webapi/search?' +
		(userId and 'user_id=' + str(userId) + '&'  or '' ) +
		(valueFrom and 'valueFrom=' + str(valueFrom) + '&'  or '' ) +
		(valueTo and 'valueTo=' + str(valueTo) + '&'  or '' ) +
		(periodFrom and 'periodFrom=' + str(periodFrom) + '&'  or '' ) +
		(periodTo and 'periodTo=' + str(periodTo) + '&'  or '' ) +
		(percentFrom and 'percentFrom=' + str(percentFrom) + '&'  or '' ) +
		(percentTo and 'percentTo=' + str(percentTo) + '&'  or '' ) +
		(status and 'status=' + str(status) + '&' or '' ) + 'key=' + self.getKey()))

'''
def main():
	webAPI = WebAPI()
	webAPI.addKey('d9cb47b739ee220bc290938262ec602b')
	print webAPI.search(status = 100).toprettyxml().encode('UTF-8')
	
if __name__ == '__main__':
	main()
'''