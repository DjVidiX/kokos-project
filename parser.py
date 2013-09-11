import re

class JAMParser():
	def __init__(self):
		self.lol = []


	"""def feed(self, string):
		string = string.replace('&lt;![CDATA[','').replace(']]&gt;', '')
		self.datas = string.split("</auction>")"""

	def getData(self, type_data, dana):
		"""if(type_data=='province'):
			try: 
				wartosc = re.search("<" + type_data + ">(.{0,50})</" + type_data + ">", dana).group(1)
				return wartosc
			except AttributeError:
				return 'Sierota nie podala wojewodztwa' """
		try:
			wartosc = re.search("<" + type_data + ">(.{0,50})</" + type_data + ">", dana).group(1)
			return wartosc
		except AttributeError:
			try:
				re.search("<" + type_data + "/>", dana).group()
				return 'Brak danych'
			except AttributeError:
				return None

	def reminderDla1300(self, dana):
		try:
			dane = re.search("<reminders>(.*)</reminders>", dana).group(1)
			try:
				if(re.search("<reminderType>REMINDER6</reminderType>", dane)):
					return 'REMINDER6'
				elif(re.search("<reminderType>REMINDER5</reminderType>", dane)):
					return 'REMINDER5'
				elif(re.search("<reminderType>REMINDER4</reminderType>", dane)):
					return 'REMINDER4'
				elif(re.search("<reminderType>REMINDER3</reminderType>", dane)):
					return 'REMINDER3'
				elif(re.search("<reminderType>REMINDER2</reminderType>", dane)):
					return 'REMINDER2'
				elif(re.search("<reminderType>REMINDER1</reminderType>", dane)):
					return 'REMINDER1'
				else:
					return 'Brak remindera'
				"""
				print lista_remindow
				if(lista_remindow.__contains__('')):
					return 'REMINDER6'
				elif(lista_remindow.__contains__('REMINDER5')):
					return 'REMINDER5'
				elif(lista_remindow.__contains__('REMINDER4')):
					return 'REMINDER4'
				elif(lista_remindow.__contains__('REMINDER3')):
					return 'REMINDER3'
				elif(lista_remindow.__contains__('REMINDER2')):
					return 'REMINDER2'
				elif(lista_remindow.__contains__('REMINDER1')):
					return 'REMINDER1'
				else:
					return 'Brak remindera'"""
			except AttributeError:
				return None
		except AttributeError:
			return None

	def reminderDla500(self, dana):
		try:
			dane = re.search("<reminders>(.*)</reminders>", dana).group(1)
			try:
				if(re.search("<reminderType>REMINDER6</reminderType>", dane)):
					return 'REMINDER6'
				else:
					return 'REMINDER5'
			except AttributeError:
				return None
		except AttributeError:
			return None
