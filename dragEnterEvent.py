from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QImageReader, QPixmap

class ImageViewer(QWidget):
    def __init__(self, parent=None):
        super(ImageViewer, self).__init__(parent)
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.label)
        self.setWindowTitle("Image Viewer")

    def setImage(self, image_path):
        reader = QImageReader(image_path)
        reader.setAutoTransform(True)
        img = reader.read()
        if not img.isNull():
            pixmap = QPixmap.fromImage(img)
            self.label.setPixmap(pixmap.scaled(self.label.size(), Qt.KeepAspectRatio))

if __name__ == '__main__':
    app = QApplication([])
    viewer = ImageViewer()
    viewer.setImage("D:\\13_python\\Python课程\\PyQt6 Python桌面开发 视频教程 2024版\\配套源码\\PyQt6Project2\\PyQt6高级控件\\rmb.png")
    viewer.show()
    app.exec_()
