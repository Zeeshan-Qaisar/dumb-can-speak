

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from register import Ui_RegisterWindow

class Ui_MainWindow(object):
    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox( )
        mess.setWindowTitle( title )
        mess.setText( message )
        mess.setStandardButtons( QtWidgets.QMessageBox.Ok )
        mess.exec_( )


    def DoLogin(self):
        email = self.email.text( )
        password = self.password.text( )
        con = pymysql.connect( host="localhost", port=3306, user="root", password="", db="dumb_can_speak" )
        cur = con.cursor( )
        query = "Select * from users Where email=%s And password=%s";
        data = cur.execute( query, (email, password) )
        if (len(cur.fetchall())>0):
            self.messagebox( "Congrats", "You have successfully Loged In" )
        else:
            self.messagebox( "Alert", "Email/Password was incorrect" )
        con.commit( )  # finalize the changes
        # Close the connection
        cur.close( )
        con.close( )

    def OpenSignUp(self):
        self.windowQtWidgets.QMainWindow()
        self.ui=Ui_RegisterWindow
        self.ui.setup(self.window)
        self.window.show()
        MainWindow.hide()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(647, 547)
        MainWindow.setStyleSheet("*{\n"
"         background: url(C:/Users/mrzes/Downloads/images/backgrund.jpg);\n"
"         background-repeat: no-repeat;\n"
"          background-size: 300px 100px;\n"
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
"#loginButton\n"
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
"    margin-top:-10px;\n"
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
        self.main.setGeometry(QtCore.QRect(100, 10, 181, 31))
        self.main.setObjectName("main")
        self.email = QtWidgets.QLineEdit(self.frame)
        self.email.setGeometry(QtCore.QRect(20, 90, 321, 41))
        self.email.setObjectName("email")
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(20, 170, 321, 41))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.loginButton = QtWidgets.QPushButton(self.frame)
        self.loginButton.setGeometry(QtCore.QRect(40, 260, 271, 41))
        self.loginButton.clicked.connect(self.DoLogin)
        self.loginButton.setObjectName("loginButton")
        self.alreadylb = QtWidgets.QLabel(self.frame)
        self.alreadylb.setGeometry(QtCore.QRect(80, 340, 141, 21))
        self.alreadylb.setObjectName("alreadylb")
        self.loginlb = QtWidgets.QLabel(self.frame)
        self.loginlb.setGeometry(QtCore.QRect(230, 340, 71, 20))
        self.loginlb.setObjectName("loginlb")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(-20, -20, 681, 551))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.raise_()
        self.frame.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 647, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.main.setText(_translate("MainWindow", "Login Here"))
        self.email.setPlaceholderText(_translate("MainWindow", "  Email"))
        self.password.setPlaceholderText(_translate("MainWindow", "  Password"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.alreadylb.setText(_translate("MainWindow", "Don\'t have an account ?"))
        self.loginlb.setText(_translate("MainWindow", "SIGN UP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
