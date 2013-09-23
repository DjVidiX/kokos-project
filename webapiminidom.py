# -*- coding: UTF-8 -*-

import gzip
import urllib
import Queue
from datetime import date
from datetime import timedelta
from math import exp
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
        return urllib.urlopen(url)
    
    def retrieveURL(self, url):
        return urllib.urlretrieve(url)[0]
    
    def getValue(self, singleNode):
        if(singleNode.childNodes):
            wartosc = str(singleNode.childNodes[0].toxml().encode('UTF-8')).replace('<![CDATA[', '').replace(']]', '').replace('>', '').replace('&oacute;', 'o')

            if(str(singleNode.nodeName) == 'province' or str(singleNode.nodeName) == 'condition'):
                province_dict={'zachodniopomorskie':'1', 'wielkopolskie':'2', 'lubelskie':'3', 'małopolskie':'4', 'dolnośląskie':'5', 'śląskie':'6', 'Śląskie':'6', 'łodzkie':'7', 'Łodzkie':'7', 'kujawsko-pomorskie':'8', 'podlaskie':'9', 'mazowieckie':'10', 'warmińsko-mazurskie':'11', 'pomorskie':'12', 'lubuskie':'13', 'podkarpackie':'14', 'opolskie':'15', 'świętokrzyskie':'16', 'Świętokrzyskie':'16', 'żonaty':'1', 'kawaler':'2', 'osoba rozwiedziona':'3', 'panna':'4', 'mężatka':'5', 'wdowa':'6', 'wdowiec':'7'}
                for key in province_dict.keys():
                    if(wartosc.lower()==key):
                        wartosc = province_dict[key]

            elif(str(singleNode.nodeName) == 'insuranceNumber'):
                if(wartosc == '0'):
                    wartosc = '1'
                else:
                    wartosc = '2'

            elif str(singleNode.nodeName) in ('identityVerificationDescription', 'employerVerificationDescription', 'identityCardVerificationDescription'):
                if(wartosc == 'pozytywna'):
                    wartosc = '2'
                else:
                    wartosc = '1'

            elif str(singleNode.nodeName) in ('createDate', 'startDate'):
                lista_daty = wartosc.split()
                data = lista_daty[0].split('-')
                data = [int(d) for d in data]
                wartosc = date(data[0], data[1], data[2])
        else:
            wartosc = 0

        return wartosc

    def getAuctionData(self, id):
        return minidom.parse(self.openURL('https://kokos.pl/webapi/get-auction-data?key=' + self.getKey() + '&id=' + str(id)))
        
    def getAuctionsByStatus(self, status):
        tempFile = self.retrieveURL('https://kokos.pl/webapi/get-auctions-by-status?key=' + self.getKey() + '&status=' + str(status))
        return minidom.parseString(gzip.open(tempFile, 'rb').read()).childNodes[0].childNodes[0].childNodes
        
    def getCurrentAuctionsWithRisk(self):
        requiredData = ['value', 'period', 'percent', 'createDate', 'insuranceNumber', 'monthlyInstallment', 'PB', 'financialVerifies']
        PB = ['startDate', 'age', 'province', 'condition', 'income', 'expenses', 'credits', 'employerVerificationDescription',
        'identityCardVerificationDescription', 'identityVerificationDescription', 'overdueDays', 'beforeDays', 'positiveRecomendations', 'negativeRecomendations']
        auctions = []
        tempAuction = {}
        currentAuctions = self.getAuctionsByStatus(100)
        for auction in currentAuctions:
            tempAuction['verify'] = 0
            for element in auction.childNodes:
                if str(element.nodeName) in requiredData:
                    if (len(element.childNodes) == 1):
                        tempAuction[str(element.nodeName)] = self.getValue(element)
                    elif (str(element.nodeName) == 'PB'):
                        for personalData in element.childNodes:
                            if str(personalData.nodeName) in PB:
                                tempAuction[str(personalData.nodeName)] = self.getValue(personalData)
                    elif (str(element.nodeName) == 'financialVerifies'):
                        tempAuction['verify'] = len(element.childNodes)
            tempAuction['risk'] = self.calcRisk(tempAuction)
            tempAuction['url'] = ('https://kokos.pl/aukcje?id=' + self.getValue(auction.getElementsByTagName('id')[0]))
            auctions.append(tempAuction)
            tempAuction = {}
        return auctions

    def getCurrentAuctions(self, *records, **inputValues):
        auctions = []
        currentAuctions = self.getCurrentAuctionsWithRisk()
        for auction in currentAuctions:
            if (float(inputValues['value']) * float(auction['percent']) >= float(inputValues['income'])) and (auction['risk'] <= inputValues['risk']) and (int(auction['period']) <= inputValues['duration']):
                 auctions.append(auction)
        return [self.convertDictionaryToList(auction, records) for auction in auctions]

    def calcRisk(self, auction):
        riskParameters = {
        'time_period': -0.0000407693375264417,
        'value': 0.0000255781166535956,
        'percent': 0.00809188866304392,
        'insuranceNumber': 0.109439160613762,
        'monthlyInstallment': -0.0000927546299863634,
        'age': 0.00128803387802354,
        'province': 0.708329946304217,
        'condition': 2.48032840681988,
        'income': 0.00000015135323567561,
        'expenses': -0.0000173713825933087,
        'credits': 0.00000279688857663816,
        'identityVerificationDescription': 0.0270154328082372,
        'employerVerificationDescription': -0.015519561345181,
        'identityCardVerificationDescription': -0.0366844766580361,
        'beforeDays': 0.000000232817562380368,
        'overdueDays': 0.0000743172705154668,
        'positiveRecomendations': -0.00128514408938851,
        'negativeRecomendations': -0.00109661386646035,
        'verify': -0.0360089281232056 }
        risk = ((riskParameters['time_period'] * float(((auction['createDate'] - auction['startDate']).total_seconds() / 60 / 60 / 24))) +
        (riskParameters['value'] * float(auction['value'])) +
        (riskParameters['percent'] * float((float(auction['percent']) * 12 / float(auction['period'])))) +
        (riskParameters['insuranceNumber'] * float(auction['insuranceNumber'])) +
        (riskParameters['monthlyInstallment'] * float(auction['monthlyInstallment'])) +
        (riskParameters['age'] * float(auction['age'])) +
        (riskParameters['province'] * 0.2313 * exp(0.0345 * float(auction['province']))) +
        (riskParameters['condition'] * 0.2439 * exp(0.0554 * float(auction['condition']))) +
        (riskParameters['income'] * float(auction['income'])) +
        (riskParameters['expenses'] * float(auction['expenses'])) +
        (riskParameters['credits'] * float(auction['credits'])) +
        (riskParameters['identityVerificationDescription'] * float(auction['identityVerificationDescription'])) +
        (riskParameters['employerVerificationDescription'] * float(auction['employerVerificationDescription'])) +
        (riskParameters['identityCardVerificationDescription'] * float(auction['identityCardVerificationDescription'])) +
        (riskParameters['beforeDays'] * float(auction['beforeDays'])) +
        (riskParameters['overdueDays'] * float(auction['overdueDays'])) +
        (riskParameters['positiveRecomendations'] * float(auction['positiveRecomendations'])) +
        (riskParameters['negativeRecomendations'] * float(auction['negativeRecomendations'])) +
        (riskParameters['verify'] * float(auction['verify'])))
        return risk

    def convertDictionaryToList(self, dicAuction, records):
        listAuction = []
        for record in records:
            if record in dicAuction:
                listAuction.append(dicAuction[record])
        listAuction.append(dicAuction['risk'])
        listAuction.append(dicAuction['url'])
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
