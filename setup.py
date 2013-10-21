from distutils.core import setup
import py2exe

Mydata_files = [('.', ['plaza.jpg', 'kokos.png']), ('imageformats', ['.\\imageformats\\qjpeg4.dll'])]

setup(
	windows=[{"script":"wywolanieGui.py"}],
	data_files = Mydata_files,
	options={"py2exe":{"includes":["sip"]}})