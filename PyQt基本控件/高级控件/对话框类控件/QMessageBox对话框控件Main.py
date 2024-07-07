import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QPushButton, QMessageBox

def showInfo():
    result = QMessageBox.information(None, '消息对话框标题', '这是一个信息对话框', QMessageBox.StandardButton.Ok)
    if result == QMessageBox.StandardButton.Ok:
        print('点击了确定按钮')

def showCritical():
    QMessageBox.critical(None, '错误对话框标题', '这是一个信息对话框', QMessageBox.StandardButton.Ok)

def showQuestion():
    QMessageBox.question(None, '问答对话框标题', '这是一个信息对话框', QMessageBox.StandardButton.Ok)

def showAbout():
    QMessageBox.about(None, '关于对话框标题', '这是一个信息对话框')

def showWarning():
    QMessageBox.warning(None, '警告对话框标题', '这是一个信息对话框', QMessageBox.StandardButton.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi('./QMessageBox对话框控件.ui')

    info_btn: QPushButton = ui.pushButton
    info_btn.clicked.connect(showInfo)

    critical_btn: QPushButton = ui.pushButton_2
    critical_btn.clicked.connect(showCritical)

    question_btn: QPushButton = ui.pushButton_3
    question_btn.clicked.connect(showQuestion)

    about_btn: QPushButton = ui.pushButton_4
    about_btn.clicked.connect(showAbout)

    warining_btn: QPushButton = ui.pushButton_5
    warining_btn.clicked.connect(showWarning)

    ui.show()

    sys.exit(app.exec())
