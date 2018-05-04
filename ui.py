#coding: utf8
#Autor: blackzero
from PyQt5.QtWebKitWidgets import QWebView, QWebPage
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from widget_scintilla import Scintilla
class AppView(QMainWindow):
	def __init__(self, *args, **kwargs):
		QMainWindow.__init__(self, *args, **kwargs)
		#интерфейс
		self.setGeometry(40, 29, 1300, 698)
		self.setWindowTitle("Hell's html debugger")

		#браузер
		self.view = QWebView()
		self.view.resize(800, 600)
		self.page = QWebPage()
		self.page.settings().setAttribute(QWebSettings.DeveloperExtrasEnabled, True)
		self.view.setPage(self.page)
		self.view.setHtml("<h1>Loading...</h1>")
		self.editor = Scintilla()
		self.editor.resize(480, 596)
		#
		widget = QWidget()

		splitter1 = QSplitter(Qt.Horizontal)
		splitter1.addWidget(self.editor)
		splitter1.addWidget(self.view)
		splitter1.setSizes([100, 200])

		hbox = QHBoxLayout()
		hbox.addWidget(splitter1)

		widget.setLayout(hbox)
		self.setCentralWidget(widget)
		self.statusBar().showMessage('Ready')
		#контекст бар
		menubar = self.menuBar()

		editor = menubar.addMenu('Редактор')
		self.editorAutoperfectly = QAction('Автовыравнивание html', self)
		editor.addAction(self.editorAutoperfectly)

		redraw = menubar.addMenu('Перемещение')
		self.redrawEditorToBrowser = QAction("Из редактора в браузера", self)
		self.redrawEditorToBrowser.setShortcut('F5')
		redraw.addAction(self.redrawEditorToBrowser)

		browser = menubar.addMenu('Браузер')
		self.helpMenu = menubar.addAction('?')

