from login import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
import pymysql

class Ui_RegisterWindow(object):

    def messagebox(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_( )

    def warningbox(self,title,message):
        mess=QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def register(self):
        username=self.username.text()
        email=self.email.text()
        password=self.password.text()
        if username!='' and email!='' and password!='':
                    if self.checkBox.isChecked( ):
                            con=pymysql.connect(host="localhost",port=3306,user="root",password="",db="dumb_can_speak")
                            cur=con.cursor()
                            query="INSERT INTO `users`(`name`, `email`, `password`) VALUES (%s,%s,%s)"
                            data=cur.execute(query,(username,email,password))
                            con.commit( )  # finalize the changes
                            # Close the connection
                            cur.close( )
                            con.close( )
                            if(data):
                                self.messagebox("Congrats","You have successfully registered")
                            else:
                                self.warningbox("Alert","Sorry Something went wrong try again")
                    else:
                        self.warningbox( "Alert", "You must check terms and conditions in order to proceed" )
        else:
            self.warningbox( "Alert", "Please fill all the required fields" )

    def openSignIn(self):
        self.Window = QtWidgets.QMainWindow( )
        self.ui = Ui_LoginWindow( )
        self.ui.setupLoginUi( self.Window )
        self.Window.show( )
        MainWindow.hide( )
    def registerUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setStyleSheet("*{\n"
        "background: url(C:/Users/mrzes/Downloads/images/backgrund.jpg);\n"
        "background-repeat: no-repeat;\n"
        "background-size: 300px 100px;\n"
        "}\n"
        "QFrame\n"
        "{\n"
        "    background:white;\n"
        "        border-radius:10px;\n"
        "\n"
        "}\n"
        "#frame_2\n"
        "{\n"
        "    background:rgba(0, 0, 0 ,0.7);\n"
        "}\n"
        "#main\n"
        "{\n"
        "    color:#005596;\n"
        "    font-size:25px;\n"
        "    font-weight:bold;\n"
        "}\n"
        "#username\n"
        "{\n"
        "    border:2px solid #AEAEAE;\n"
        "    border-radius:5px;\n"
        "    background:white;\n"
        "    font-weight:bold;\n"
        "}\n"
        "#email\n"
        "{\n"
        "    border:2px solid #AEAEAE;\n"
        "    border-radius:5px;\n"
        "    background:white;\n"
        "    font-weight:bold;\n"
        "}\n"
        "#password\n"
        "{\n"
        "    border:2px solid #AEAEAE;\n"
        "    border-radius:5px;\n"
        "    background:white;\n"
        "    font-weight:bold;\n"
        "}\n"
        "#registerButton\n"
        "{\n"
        "    font-size:18px;\n"
        "    color:white; \n"
        "    background:#005596;\n"
        "    border:none;\n"
        "    border-radius:5px;\n"
        "}\n"
        "#alreadylb\n"
        "{\n"
        "    font-size:13px;\n"
        "    margin-top:5px;\n"
        "}\n"
        "#loginlb\n"
        "{\n"
        "    color:#005596;\n"
        "    font-weight:bold;\n"
        "    text-decoration:underline;\n"
        "    margin-top:5px;\n"
        "    background:transparent;\n"
        "}\n"
        "QCheckBox\n"
        "{\n"
        "    background:white;\n"
        "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(150, 30, 371, 381))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.main = QtWidgets.QLabel(self.frame)
        self.main.setGeometry(QtCore.QRect(90, 10, 181, 31))
        self.main.setObjectName("main")
        self.username = QtWidgets.QLineEdit(self.frame)
        self.username.setGeometry(QtCore.QRect(20, 80, 321, 41))
        self.username.setObjectName("username")
        self.email = QtWidgets.QLineEdit(self.frame)
        self.email.setGeometry(QtCore.QRect(20, 140, 321, 41))
        self.email.setObjectName("email")
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(20, 200, 321, 41))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.registerButton = QtWidgets.QPushButton(self.frame)
        self.registerButton.setGeometry(QtCore.QRect(40, 290, 271, 41))
        self.registerButton.setCursor( QCursor( QtCore.Qt.PointingHandCursor ) )
        self.registerButton.setObjectName("registerButton")
        self.registerButton.clicked.connect(self.register)
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(20, 250, 241, 31))
        self.checkBox.setObjectName("checkBox")
        self.alreadylb = QtWidgets.QLabel(self.frame)
        self.alreadylb.setGeometry(QtCore.QRect(80, 340, 151, 21))
        self.alreadylb.setObjectName("alreadylb")
        self.loginlb = QtWidgets.QPushButton(self.frame)
        self.loginlb.setGeometry(QtCore.QRect(230, 340, 71, 20))
        self.loginlb.clicked.connect( self.openSignIn )
        self.loginlb.setCursor( QCursor( QtCore.Qt.PointingHandCursor ) )
        self.loginlb.setObjectName("loginlb")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, -20, 681, 551))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.raise_()
        self.frame.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Register"))
        self.main.setText(_translate("MainWindow", "Register Here"))
        self.username.setPlaceholderText(_translate("MainWindow", "  User Name"))
        self.email.setPlaceholderText(_translate("MainWindow", "  Email"))
        self.password.setPlaceholderText(_translate("MainWindow", "  Password"))
        self.registerButton.setText(_translate("MainWindow", "Create an account"))
        self.checkBox.setText(_translate("MainWindow", "I Accept the Terms And Conditions"))
        self.alreadylb.setText(_translate("MainWindow", "Already have an account ?"))
        self.loginlb.setText(_translate("MainWindow", "LOGIN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_RegisterWindow()
    ui.registerUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
