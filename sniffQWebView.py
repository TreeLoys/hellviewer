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
		#для перехвата исходящих post запросов
		transit_data = None
		if device:

			transit = device.peek(1024)
			print transit
			return QNetworkAccessManager.createRequest(self, operation, request, device)
		else:
			return QNetworkAccessManager.createRequest(self, operation, request, device)
		#пример device и работа же сним для изменения post переменных
		# (последний пост)
		#https://stackoverflow.com/questions/26630961/how-to-change-post-data-in-qtwebkit
		#пример после отпавки данных ка спарсить ответ
		#https://stackoverflow.com/questions/34405133/python-pyqt5-subclassing-qnetworkaccessmanagercreaterequest-data-duplication
		#огромный пример для постабработки
		#https://stackoverflow.com/questions/15988988/how-to-forge-request-using-createrequest-by-subclassing-qnetworkaccessmanager

		#огромное внедрение протокола
		#https://wiki.python.org/moin/PyQt/Adding%20the%20Gopher%20Protocol%20to%20QtWebKit
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

		#view.setUrl(QUrl('http://mathan/'))
		self.show()
		view.setUrl(QUrl('http://spaces.ru/'))


if __name__ == "__main__":

	app = QApplication(sys.argv)
	ui = App()
	app.exec_()
