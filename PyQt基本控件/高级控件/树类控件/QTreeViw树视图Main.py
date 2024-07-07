import sys

from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QFileSystemModel
from PyQt6.QtWidgets import QApplication, QTreeView

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = uic.loadUi('./QTreeView树视图.ui')

    myTreeView: QTreeView = ui.treeView

    model = QStandardItemModel()
    model.setHorizontalHeaderLabels(['分类', '书名', '作者', '价格'])
    boolType1 = QStandardItem('JAVA类')  # 添加一级节点
    boolType1.appendRow([QStandardItem('JAVA入门'), QStandardItem('1'), QStandardItem('2'), QStandardItem('10')])  # 添加二级节点
    model.appendRow(boolType1)

    boolType2 = QStandardItem('PY类')  # 添加一级节点
    boolType2.appendRow(
        [QStandardItem('JAVA入门'), QStandardItem('1'), QStandardItem('2'), QStandardItem('10')])  # 添加二级节点
    model.appendRow(boolType2)

    boolType3 = QStandardItem('GO类')  # 添加一级节点
    boolType3.appendRow(
        [QStandardItem('JAVA入门'), QStandardItem('1'), QStandardItem('2'), QStandardItem('10')])  # 添加二级节点
    model.appendRow(boolType3)

    myTreeView.setModel(model)
    myTreeView.expandAll()
    ui.show()

    sys.exit(app.exec())
