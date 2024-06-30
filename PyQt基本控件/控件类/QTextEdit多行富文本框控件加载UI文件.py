from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QTextEdit
from PyQt6 import uic, QtGui
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi('./QTextEdit多行富文本框空间.ui')
    myTextEdit: QTextEdit = ui.textEdit
    myTextEdit_2: QTextEdit = ui.textEdit_2
    myTextEdit.setTextColor(QtGui.QColor(255, 0, 0))
    myTextEdit.setTextBackgroundColor(QtGui.QColor(0, 255, 0))
    myTextEdit.setPlainText("77KFC")
    myTextEdit_2.setHtml("77<font color = 'red'>K</font>, <a href = 'www.bing.com'>FC</href>")

    print(myTextEdit.toPlainText())
    print(myTextEdit.toHtml())

    ui.show()

    sys.exit(app.exec())
