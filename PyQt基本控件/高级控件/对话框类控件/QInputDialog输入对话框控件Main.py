import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QPushButton, QMessageBox, QFileDialog, QLabel, QLineEdit, QInputDialog


def getName(formLayoutWidget, name_input):
    name, ok = QInputDialog.getText(formLayoutWidget, '姓名', '请输入姓名', QLineEdit.EchoMode.Normal, '77KFC')   # 获取输入的姓名
    if ok:
        name_input.setText(name)

def getGrade(formLayoutWidget, class_input):
    grade, ok = QInputDialog.getItem(formLayoutWidget, '班级', '请选择班级', (['1班', '2班', '3班', '4班', '5班', '6班', '7班', '8班', '9班', '10班']), 0, False)  # 获取输入的班级)
    if ok:
        class_input.setText(grade)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi('./QInputDialog输入对话框控件.ui')

    formLayoutWidget = ui.formLayoutWidget

    name_input: QLineEdit = ui.lineEdit
    name_input.returnPressed.connect(lambda: getName(formLayoutWidget, name_input))

    age_input: QLineEdit = ui.lineEdit_2

    class_input: QLineEdit = ui.lineEdit_3
    class_input.returnPressed.connect(lambda: getGrade(formLayoutWidget, class_input))

    num_input: QLineEdit = ui.lineEdit_4

    ui.show()

    sys.exit(app.exec())
