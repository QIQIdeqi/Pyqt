import sys

from PyQt6 import uic
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QTabWidget, QWidget

if __name__ == '__main__':
    # 创建应用程序对象
    app = QApplication(sys.argv)

    # 加载UI文件
    ui = uic.loadUi('./QTabWidget容器.ui')

    tab = QWidget()

    # 获取控件对象
    myTabWidget: QTabWidget = ui.tabWidget

    addTab = myTabWidget.addTab(tab, "标签1")

    tab2 = QWidget()

    myTabWidget.addTab(tab2, QIcon('3.png'), "标签2")

    ui.show()

    # 进入程序的主循环，并通过exit确保主循环安全结束
    sys.exit(app.exec())
