import sys

from PyQt6 import uic
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QToolBox

if __name__ == '__main__':
    # 创建应用程序对象
    app = QApplication(sys.argv)

    # 加载UI文件
    ui = uic.loadUi('./QToolBox容器.ui')

    myToolBox: QToolBox = ui.toolBox

    tab1 = QWidget()

    myToolBox.addItem(tab1, "测试")

    tab2 = QWidget()

    myToolBox.addItem(tab2, QIcon("./1.png"), "测试2")

    ui.show()

    # 进入程序的主循环，并通过exit确保主循环安全结束
    sys.exit(app.exec())
