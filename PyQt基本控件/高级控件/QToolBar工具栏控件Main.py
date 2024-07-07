import sys

from PyQt6 import uic
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QToolBar

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi('./QToolBar工具栏控件.ui')

    myToolBar: QToolBar = ui.toolBar

    # 添加一个添加按钮
    myToolBar.addAction(QIcon('./add2.png'), '添加')

    # 添加一个分隔符
    myToolBar.addSeparator()

    # 添加一个保存按钮
    myToolBar.addAction(QIcon('./save.png'), '保存')

    ui.show()

    sys.exit(app.exec())
