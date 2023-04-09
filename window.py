import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QStackedWidget, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPixmap, QIcon, QImage
from PyQt5.QtCore import pyqtSlot, QTimer

from camera import Camera
scan = -1

class LoginWindow(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()

        self.stacked_widget = stacked_widget

        username_label = QLabel("Username")
        self.username_field = QLineEdit()
        password_label = QLabel("Password")
        self.password_field = QLineEdit()
        self.password_field.setEchoMode(QLineEdit.Password)

        login_button = QPushButton("Login")
        login_button.clicked.connect(self.login)

        layout = QVBoxLayout()
        layout.addWidget(username_label)
        layout.addWidget(self.username_field)
        layout.addSpacing(10)
        layout.addWidget(password_label)
        layout.addWidget(self.password_field)
        layout.addSpacing(20)
        layout.addWidget(login_button)
        layout.setObjectName("login_page")

        self.setLayout(layout)
        layout.setContentsMargins(450, 200, 450, 100)


       # Add spacer items to center login content in window
        spacer_top = QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)
        spacer_bottom = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addSpacerItem(spacer_top)
        layout.addSpacerItem(spacer_bottom) 

    # # Create layouts
    #     vbox = QVBoxLayout()
    #     hbox1 = QHBoxLayout()
    #     hbox2 = QHBoxLayout()

    #     # Add widgets to layouts
    #     hbox1.addWidget(username_label)
    #     hbox1.addWidget(self.username_field)
    #     hbox2.addWidget(password_label)
    #     hbox2.addWidget(self.password_field)
    #     vbox.addLayout(hbox1)
    #     vbox.addLayout(hbox2)
    #     vbox.addWidget(login_button)

    #     # Add spacers to center widgets
    #     vertical_spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
    #     horizontal_spacer1 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
    #     horizontal_spacer2 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
    #     vbox.addItem(vertical_spacer)
    #     vbox.addItem(horizontal_spacer1)
    #     vbox.addItem(horizontal_spacer2)

    #     # Set the main layout
    #     self.setLayout(vbox)

        # # Set the margins around the content
        # vbox.setContentsMargins(250, 50, 250, 50)

    def login(self):
        # Check if username and password are correct
        if self.username_field.text() == "admin" and self.password_field.text() == "admin":
            # Switch to home page
            self.stacked_widget.setCurrentIndex(1)


class HomePage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()

        self.stacked_widget = stacked_widget

        welcome_label = QLabel("Welcome to Contactless Payment!")
        welcome_label.setObjectName("headingLabel")

        process_label = QLabel("  Scan  >  Register  >  Pay")

        register_button = QPushButton(" New User")
        # register_button.setIcon(QIcon('images/new_user.png'))
        payment_button = QPushButton(" Checkout")
        # payment_button.setIcon(QIcon('images/checkout.png'))
        register_button.setObjectName('headingLabel')
        payment_button.setObjectName('headingLabel')
        register_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        payment_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        register_button.clicked.connect(lambda: self.change_page(0))
        payment_button.clicked.connect(lambda: self.change_page(1))

        v_layout = QVBoxLayout()
        v_layout.addWidget(welcome_label)
        v_layout.addSpacing(10)
        v_layout.addWidget(process_label)
        v_layout.addSpacing(20)

        h_layout = QHBoxLayout()
        h_layout.addWidget(register_button)
        h_layout.addSpacing(20)
        h_layout.addWidget(payment_button)

        v_layout.addLayout(h_layout)
        self.setLayout(v_layout)
        v_layout.setContentsMargins(100, 100, 100, 100)

    def change_page(self, data):
        global scan 
        scan = data
        self.stacked_widget.setCurrentIndex(2)


# import cv2
# from roiExtraction import ROIExtractor
# import threading, time

# class ScanPage(QWidget):
#     def __init__(self, stacked_widget):
#         super().__init__()
#         self.cap = cv2.VideoCapture(0)

#         self.stacked_widget = stacked_widget

#         layout = QVBoxLayout()

#         welcome_label = QLabel("Please place your palm on the camera")
#         welcome_label.setObjectName("headingLabel")

#         self.ROI_video_label = QLabel(self)
#         self.ROI_video_label.resize(200, 200)

#         self.live_video_label = QLabel(self)
#         self.live_video_label.resize(200, 200)

#         button1 = QPushButton('Open Camera', self)
#         button1.clicked.connect(self.get_frame)

#         button2 = QPushButton('Take Picture',self)
#         button2.clicked.connect(self.get_roi)

#         layout.addWidget(welcome_label)
#         layout.addSpacing(20)
#         h1_layout = QHBoxLayout()
#         h1_layout.addWidget(button1)
#         layout.addSpacing(20)
#         h1_layout.addWidget(button2)
#         layout.addSpacing(20)
#         h_layout = QHBoxLayout()
#         h_layout.addWidget(self.ROI_video_label)
#         h_layout.addSpacing(20)
#         h_layout.addWidget(self.live_video_label)

#         layout.addLayout(h1_layout)
#         layout.addLayout(h_layout)
#         self.setLayout(layout)
#         layout.setContentsMargins(100,100,100,100)

#     # def show_roi(self):
#     #     pixmap = QPixmap('ROI.jpg')
#     #     # Create QLabel object and set the pixmap as its content
#     #     lbl = QLabel(self)
#     #     lbl.setPixmap(pixmap)
#     #     lbl.setGeometry(50, 200, pixmap.width(), pixmap.height())

#     #     lbl.update()
#     #     self.update()
#     #     # print("Image Updated")
    
#     # def get_frame(self):
#     #     self.timer = QTimer()
#     #     self.timer.timeout.connect(self.display_frame)
#     #     self.timer.start(30)

#     def get_frame(self):
#         while True:
#             # t1 = threading.Thread()
#             # t1.start()
#             ret, frame = self.cap.read()

#             gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#             self.frame = ROIExtractor().extract(gray)

#             roi = QImage(self.frame.data, self.frame.shape[1], self.frame.shape[0], QImage.Format_RGB888)
#             roi = roi.rgbSwapped()
#             live = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
#             live = live.rgbSwapped()

#             # t1.join()
#             pixmap2 = QPixmap.fromImage(live)
#             self.live_video_label.setPixmap(pixmap2)
#             pixmap1 = QPixmap.fromImage(roi)
#             self.ROI_video_label.setPixmap(pixmap1)
#             time.sleep(0.03)

#             # cv2.namedWindow("Hand Palm Detection", cv2.WINDOW_NORMAL)
#             # cv2.resizeWindow("Hand Palm Detection", 300, 300)
#             # cv2.imshow('Hand Palm Detection', self.frame)
#             # cv2.imshow('Live feedback', gray)

#     def get_live(self):
#         _, frame = self.cap.read()
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         return frame

#     def get_roi(self):
#         status = cv2.imwrite("ROI.jpg", self.frame)
#         print(f"Image saved - {status}")
#         self.cap.release()
#         cv2.destroyAllWindows()
#         # self.show_roi()

#     def __del__(self):
#         self.cap.release()

#     # def closeEvent(self, event):
#     #     self.capture.release()
#     #     event.accept()


class _ScanPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

        layout = QVBoxLayout()

        welcome_label = QLabel("Please place your palm on the camera")
        welcome_label.setObjectName("headingLabel")

        button1 = QPushButton('Open Camera', self)
        button1.clicked.connect(self.get_frame)

        button2 = QPushButton('Take Picture',self)
        button2.clicked.connect(self.get_roi)

        layout.addWidget(welcome_label)
        layout.addSpacing(20)
        h1_layout = QHBoxLayout()
        h1_layout.addWidget(button1)
        layout.addSpacing(20)
        h1_layout.addWidget(button2)
        layout.addSpacing(20)
        h_layout = QHBoxLayout()
        h_layout.addSpacing(20)

        layout.addLayout(h1_layout)
        layout.addLayout(h_layout)
        self.setLayout(layout)
        layout.setContentsMargins(100,100,100,100)
    
    @pyqtSlot()
    def get_frame(self):
        self.cam = Camera()
        self.cam.get_frame()

    @pyqtSlot()
    def get_roi(self):
        try:
            status = self.cam.get_roi()
            print(f"Image saved - {status}")
            
            if scan == 0:
                self.stacked_widget.setCurrentIndex(3)
            elif scan == 1:
                self.stacked_widget.setCurrentIndex(4)
        except Exception as ex:
            print(ex)


class MatchPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

        layout = QVBoxLayout()
        welcome_label = QLabel("Matching Please Wait...")
        welcome_label.setObjectName("headingLabel")

        pixmap = QPixmap("ROI.jpg")
        self.ROI_label = QLabel(self)
        # self.ROI_label.resize(250, 250)
        self.ROI_label.setPixmap(pixmap)

        layout.addWidget(welcome_label)
        layout.addSpacing(20)
        layout.addWidget(self.ROI_label)
        self.setLayout(layout)
        layout.setContentsMargins(100, 100, 100, 100)

    # def show_roi(self):
    #     pixmap = QPixmap('ROI.jpg')
    #     # Create QLabel object and set the pixmap as its content
    #     lbl = QLabel(self)
    #     lbl.setPixmap(pixmap)
    #     lbl.setGeometry(50, 200, pixmap.width(), pixmap.height())
    #     # print("Image Updated")

class RegisterPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

class MainWindow(QMainWindow):
    def __init__(self, W_width, w_height):
        super().__init__()

        self.setWindowTitle("Contactless Payment")
        self.setGeometry(0, 0, W_width, w_height)

        stacked_widget = QStackedWidget()
        login_page = LoginWindow(stacked_widget)
        home_page = HomePage(stacked_widget)
        # scan_page = ScanPage(stacked_widget)
        scan_page = _ScanPage(stacked_widget)
        register_page = RegisterPage(stacked_widget)
        match_page = MatchPage(stacked_widget)
        

        stacked_widget.addWidget(login_page) 
        stacked_widget.addWidget(home_page)
        stacked_widget.addWidget(scan_page)
        stacked_widget.addWidget(register_page)
        stacked_widget.addWidget(match_page)


        self.setCentralWidget(stacked_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    rect = screen.availableGeometry()

    with open('style.qss', 'r') as f:
        style = f.read()
    app.setStyleSheet(style)

    app_icon = QIcon('images/palmscan.png')
    app.setWindowIcon(app_icon)

    window = MainWindow(rect.width(),rect.height())
    window.show()
    sys.exit(app.exec_())
