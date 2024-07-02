import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QComboBox, QGroupBox

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi('./QComboBox控件.ui')
    myComboBox: QGroupBox = ui.groupBox

    myComboBox.setChecked(False)

    ui.show()

    sys.exit(app.exec())
