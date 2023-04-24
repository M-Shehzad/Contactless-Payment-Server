import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap, QImage


from camera import Camera

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Payment using Palm'
        self.left = 30
        self.top = 30
        self.width = 480
        self.height = 640
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button1 = QPushButton('Open Camera', self)
        # button1.setToolTip('This is an example button')
        button1.move(100,70)
        button1.clicked.connect(self.get_frame)

        button2 = QPushButton('Take Picture',self)
        button2.move(250,70)
        button2.clicked.connect(self.get_roi)

        self.show_roi()

        self.show()

    def show_roi(self):
        pixmap = QPixmap('ROI.jpg')
        # Create QLabel object and set the pixmap as its content
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        lbl.setGeometry(50, 200, pixmap.width(), pixmap.height())

        lbl.update()
        self.update()
        # print("Image Updated")


    @pyqtSlot()
    def get_frame(self):
        self.cam = Camera()
        self.cam.get_frame()
        # frame = cam.get_live()
        # height, width, channel = frame.shape
        # bytesPerLine = 3 * width

        # # Create QImage from the OpenCV image data
        # qImg = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)

        # # Create QPixmap from the QImage object
        # pixmap = QPixmap.fromImage(qImg)

        # lbl = QLabel(self)
        # lbl.setPixmap(pixmap)
        # lbl.setGeometry(0, 0, width, height)


    @pyqtSlot()
    def get_roi(self):
        status = self.cam.get_roi()
        print(f"Image saved - {status}")
        self.show_roi()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())