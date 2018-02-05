#coding: utf8
#Autor: blackzero
from PyQt5.QtWebKitWidgets import QWebView, QWebPage
from PyQt5.QtWidgets import *
from PyQt5.QtNetwork import *
from PyQt5.QtCore import *
import os, sys
class CostumQNetworkReply(QNetworkReply):
	def __init__(self):
		QNetworkReply.__init__(self)
"""
def afterReply(reply):
	er = reply.error()
	if er == QNetworkReply.NoError:
		bytes_string = reply.readAll()
		print(str(bytes_string, 'utf-8'))
	else:
		print "Error response"""
class CostumQNetworkAccessManager(QNetworkAccessManager):
	def __init__(self):
		QNetworkAccessManager.__init__(self)
	def createRequest(self, operation, request, device):
		"""print (("Status: %s Url: %s")%(request.header(),
									  request.url()))"""
		return QNetworkAccessManager.createRequest(self, operation, request, device)
class App(QWidget):
	def __init__(self, *args, **kwargs):
		QWidget.__init__(self, *args, **kwargs)
		view = QWebView(self)
		view.resize(800, 600)
		#view.setHtml("<h1>Loading...</h1>")
		#для перехвата post
		page = QWebPage()
		cm = CostumQNetworkAccessManager()
		#cm.finished.connect(afterReply)
		page.setNetworkAccessManager(cm)
		view.setPage(page)
		"""
		noth = view.page().networkAccessManager()
		print (noth)
		print (cm)
		view.page().setNetworkAccessManager(cm)
		"""
		#view.setUrl(QUrl('http://mathan/'))
		self.show()
		view.setUrl(QUrl('http://spaces.ru/'))


if __name__ == "__main__":

	app = QApplication(sys.argv)
	ui = App()
	app.exec_()
