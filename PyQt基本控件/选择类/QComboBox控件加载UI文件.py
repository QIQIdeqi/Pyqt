from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QComboBox
from PyQt6 import uic
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi('./QComboBox控件.ui')

    myComBox: QComboBox = ui.comboBox  # 获取QComboBox控件
    myLabel: QLabel = ui.label  # 获取QLabel控件

    myComBox.addItems(['Python', 'C++', 'Java', 'Go', 'JavaScript'])
    myComBox.addItem(QIcon('./icon/other.png'), 'Other')
    current_Text = myComBox.currentText()

    myLabel.setText(current_Text)

    ui.show()

    sys.exit(app.exec())
