import sys

from PyQt6 import uic
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QToolBar, QStatusBar, QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi('./QStatusBar状态栏控件.ui')

    myStatusBar: QStatusBar = ui.statusBar

    myLabel = QLabel()
    myLabel.setText("版权所有：77KFC")

    myStatusBar.addWidget(myLabel)

    myLabel_2 = QLabel()
    myLabel_2.setText("版权所有：77KFC")

    myStatusBar.addPermanentWidget(myLabel_2)

    myStatusBar.removeWidget(myLabel)
    myStatusBar.showMessage("当前登录用户：77KFC", 5000)

    ui.show()

    sys.exit(app.exec())
