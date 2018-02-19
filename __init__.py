#coding: utf8

from PyQt5.QtWebKitWidgets import QWebView, QWebPage
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys
from ui import AppView
from bs4 import BeautifulSoup
class DebugBrowser(AppView):
	def __init__(self, *args, **kwargs):
		AppView.__init__(self, *args, **kwargs)
		self.base_url = None
		self.coef_view = 0

		#привязка событий
		self.redrawEditorToBrowser.triggered.connect(self.rerolHtml)
		self.editorAutoperfectly.triggered.connect(self.bs_perfect)
		self.helpMenu.triggered.connect(self.help)
		self.show()
	def help(self):
		QMessageBox.about(self, "Привет!", """\n
Гайд по дебаггеру:\n
F5 - быстрое обновление
		""")
	def bs_perfect(self):
		t = BeautifulSoup(self.editor.text(),"lxml")
		self.editor.setText(t.prettify())

	def rerolHtml(self):
		self.setHtml(self.editor.text())
	def setHtml(self, html, base_url=None):
		self.editor.setText(html)
		if base_url:
			self.base_url = base_url
		if self.base_url:
			self.view.setHtml(html, QUrl(self.base_url))
		else:
			self.view.setHtml(html)
	def showRequestsTable(self):
		pass
def show_debug_browser(data, base_url=None):
	app = QApplication(sys.argv)
	exe = DebugBrowser()
	exe.setHtml(data, base_url)
	app.exec_()
if __name__ == "__main__":
	show_debug_browser("<h1>Welcome to hell's debuger</h1>")