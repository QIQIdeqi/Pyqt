from PyQt6.QtWidgets import QApplication, QLabel
from PyQt6 import uic
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi('./QLabel标签控件.ui')

    myLabel: QLabel = ui.label
    print(myLabel.text())
    ui.show()

    sys.exit(app.exec())
