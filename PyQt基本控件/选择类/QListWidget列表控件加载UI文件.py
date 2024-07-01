import sys

from PyQt6 import uic
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QLabel, QListWidget, QListWidgetItem

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi('./QListWidget控件列表控件.ui')

    myListWidget: QListWidget = ui.listWidget

    lwItem = QListWidgetItem()
    lwItem.setText('PyQt6')
    myListWidget.addItem(lwItem)

    ui.show()

    sys.exit(app.exec())
