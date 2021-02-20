
from profile import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor

class Ui_Home(object):
    def openProfile(self):
        self.registerWindow=QtWidgets.QMainWindow()
        self.ui=Ui_Profile()
        self.ui.setupProfileUi(self.registerWindow)
        self.registerWindow.show()
        MainWindow.hide()


    def setupUi(self, Home):
        Home.setObjectName("Home")
        height = 640
        # setting  the fixed height of window
        Home.setFixedHeight( height )
        width = 1080
        # setting  the fixed width of window
        Home.setFixedWidth( width )
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/Camera.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Home.setWindowIcon(icon)
        Home.setStyleSheet("#centralwidget\n"
        "{\n"
        " background-color:black;\n"
        "}\n"
        "#camera\n"
        "{\n"
        " background-color:gray;\n"
        "}\n"
        "#head\n"
        "{\n"
        "    font-size:20px;\n"
        "  color:white;\n"
        "}\n"
        "#word\n"
        "{\n"
        "    font-size:30px;\n"
        "    color:white;\n"
        "}\n"
        "#syntance\n"
        "{\n"
        "    font-size:18px;\n"
        "    color:white;\n"
        "}\n"
        "\n"
        ".QPushButton\n"
        "{\n"
        " border:none;\n"
        "background-color:transparent;\n"
        "color:white;\n"
        "font-size:18px;\n"
        "}\n"
        "\n"
        ".QPushButton:hover\n"
        "{\n"
        "    cursor: pointer;\n"
        "}\n"
        "#CameraIcon,#profileIcon\n"
        "{\n"
        "  text-align:center;\n"
        "padding-left:10px;\n"
        "}")
        self.centralwidget = QtWidgets.QWidget(Home)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 69, 241, 221))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(70, 410, 121, 161))
        self.widget.setObjectName("widget")
        self.CameraIcon = QtWidgets.QLabel(self.widget)
        self.CameraIcon.setGeometry(QtCore.QRect(10, 120, 61, 51))
        self.CameraIcon.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CameraIcon.setText("")
        self.CameraIcon.setPixmap(QtGui.QPixmap("icons/videocam-24px.png"))
        self.CameraIcon.setScaledContents(True)
        self.CameraIcon.setObjectName("CameraIcon")
        self.camera = QtWidgets.QFrame(self.centralwidget)
        self.camera.setGeometry(QtCore.QRect(-1, -1, 701, 511))
        self.camera.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.camera.setFrameShadow(QtWidgets.QFrame.Raised)
        self.camera.setObjectName("camera")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 570, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 570, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 570, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.head = QtWidgets.QLabel(self.centralwidget)
        self.head.setGeometry(QtCore.QRect(780, 10, 231, 31))
        self.head.setObjectName("head")
        self.word = QtWidgets.QLabel(self.centralwidget)
        self.word.setGeometry(QtCore.QRect(770, 40, 41, 51))
        self.word.setObjectName("word")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(770, 80, 231, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.syntance = QtWidgets.QLabel(self.centralwidget)
        self.syntance.setGeometry(QtCore.QRect(770, 110, 131, 16))
        self.syntance.setObjectName("syntance")
        self.profileIcon = QtWidgets.QLabel(self.centralwidget)
        self.profileIcon.setGeometry(QtCore.QRect(320, 540, 41, 31))
        self.profileIcon.setText("")
        self.profileIcon.setPixmap(QtGui.QPixmap("icons/Path 10.png"))
        self.profileIcon.setScaledContents(True)
        self.profileIcon.setObjectName("profileIcon")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(560, 540, 41, 31))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icons/Path 6.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.mic = QtWidgets.QLabel(self.centralwidget)
        self.mic.setGeometry(QtCore.QRect(920, 470, 31, 41))
        self.mic.setText("")
        self.mic.setPixmap(QtGui.QPixmap("icons/Speaker.png"))
        self.mic.setScaledContents(True)
        self.mic.setObjectName("mic")
        Home.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Home)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 21))
        self.menubar.setObjectName("menubar")
        Home.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Home)
        self.statusbar.setObjectName("statusbar")
        Home.setStatusBar(self.statusbar)

        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home):
        _translate = QtCore.QCoreApplication.translate
        Home.setWindowTitle(_translate("Home", "Home"))
        self.pushButton.setText(_translate("Home", "Start"))
        self.pushButton_2.setText(_translate("Home", "Profile"))
        self.pushButton_2.clicked.connect( self.openProfile )
        self.pushButton_2.setCursor( QCursor( QtCore.Qt.PointingHandCursor ) )
        self.pushButton_3.setText(_translate("Home", "History"))
        self.head.setText(_translate("Home", "Hand Gesture into text"))
        self.word.setText(_translate("Home", "H"))
        self.syntance.setText(_translate("Home", "How are you ?"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Home()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())