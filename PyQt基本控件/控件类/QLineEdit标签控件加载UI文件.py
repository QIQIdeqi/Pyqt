from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton
from PyQt6 import uic
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi('./QLineEdit单行文本框.ui')

    myLineEdit: QLineEdit = ui.lineEdit
    myLabel: QLabel = ui.label

    myButton: QPushButton = ui.pushButton
    myButton.clicked.connect(lambda: myLabel.setText(myLineEdit.text()))

    # 输出文本框中的文本
    print(myLineEdit.text())
    ui.show()

    sys.exit(app.exec())
