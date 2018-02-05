#coding: utf8
from PyQt5.Qsci import QsciScintilla, QsciLexerHTML
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMenu, QApplication, qApp


class LexerHTML(QsciLexerHTML):
	def __init__(self, *args, **kwargs):
		super(LexerHTML, self).__init__(*args, **kwargs)
		font = QFont()
		font.setFamily('Courier New')
		font.setFixedPitch(True)
		font.setPointSize(13)
		self.setFont(font)
class Scintilla(QsciScintilla):
	def __init__(self, *args, **kwargs):
		QsciScintilla.__init__(self, *args, **kwargs)
		self.setLexer(LexerHTML())
		self.setIndentationGuides(True)
		self.setAutoIndent(True)
		self.setMarginWidth(1, 35)
		self.setMarginLineNumbers(1, True)
		self.setUtf8(True)
		self.setAutoCompletionCaseSensitivity(False)
		self.setAutoCompletionReplaceWord(False)
		self.setAutoCompletionSource(QsciScintilla.AcsDocument)
		self.setAutoCompletionThreshold(1)
	def contextMenuEvent(self, event):
		menu = QMenu(self)
		wrapAction = menu.addAction("Раскрасить")
		quitAction = menu.addAction("Выход")
		action = menu.exec_(self.mapToGlobal(event.pos()))
		if action == wrapAction:
			QApplication.clipboard().setText(" style='background-color: #fef;'")
			self.paste()
		if action == quitAction:
			qApp.quit()