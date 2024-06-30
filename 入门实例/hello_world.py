"""
    第一个pyqt6程序
"""

from PyQt6.QtWidgets import QApplication, QWidget, QLabel
import sys

app = QApplication(sys.argv)  # 创建一个应用
#   print(sys.argv) 打印文件目录
#   print(app.arguments())  打印文件目录

window = QWidget()
window.setWindowTitle("第一个pyqt6程序")
window.resize(500, 500)
window.move(0, 0)
window.show()

label = QLabel()
label.setText("Hello World!")
label.move(100, 100)
label.resize(200, 100)
label.setStyleSheet("background-color: yellow;padding:10px")
label.setParent(window)
label.show()

sys.exit(app.exec())  # 开始执行程序，并且进去消息循环等待
