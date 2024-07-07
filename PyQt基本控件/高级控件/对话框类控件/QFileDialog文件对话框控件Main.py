import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QPushButton, QMessageBox, QFileDialog


def selectFile():
    fd = QFileDialog()
    fd.setFileMode(QFileDialog.FileMode.ExistingFiles)  # 设置文件对话框模式为选择文件
    fd.setDirectory('c:\\') # 设置默认打开的路径
    fd.setNameFilters(["Image Files (*.jpg *.png *.gif)"]) # 设置文件过滤器'
    if fd.exec():
        print(fd.selectedFiles())

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi('./QFileDialog文件对话框控件.ui')

    info_btn: QPushButton = ui.pushButton
    info_btn.clicked.connect(selectFile)

    ui.show()

    sys.exit(app.exec())
