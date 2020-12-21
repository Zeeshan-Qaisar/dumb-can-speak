# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginPage(object):
    def setupUi(self, LoginPage):
        LoginPage.setObjectName("LoginPage")
        LoginPage.resize(561, 497)
        LoginPage.setWindowOpacity(0.0)
        LoginPage.setStyleSheet("*{\n"
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
"    margin-top:-10px;\n"
"}\n"
"QCheckBox\n"
"{\n"
"    background:white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(LoginPage)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(140, 20, 371, 381))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.LoginHere = QtWidgets.QLabel(self.frame)
        self.LoginHere.setGeometry(QtCore.QRect(120, 40, 141, 31))
        self.LoginHere.setObjectName("LoginHere")
        self.EnterEmail = QtWidgets.QLineEdit(self.frame)
        self.EnterEmail.setGeometry(QtCore.QRect(20, 120, 321, 41))
        self.EnterEmail.setObjectName("EnterEmail")
        self.EnterPassword = QtWidgets.QLineEdit(self.frame)
        self.EnterPassword.setGeometry(QtCore.QRect(20, 180, 321, 41))
        self.EnterPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.EnterPassword.setObjectName("EnterPassword")
        self.registerButton = QtWidgets.QPushButton(self.frame)
        self.registerButton.setGeometry(QtCore.QRect(50, 260, 271, 41))
        self.registerButton.setObjectName("registerButton")
        self.TermsandConditions = QtWidgets.QCheckBox(self.frame)
        self.TermsandConditions.setGeometry(QtCore.QRect(20, 220, 241, 31))
        self.TermsandConditions.setObjectName("TermsandConditions")
        self.AlreadyAccount = QtWidgets.QLabel(self.frame)
        self.AlreadyAccount.setGeometry(QtCore.QRect(80, 310, 151, 21))
        self.AlreadyAccount.setObjectName("AlreadyAccount")
        self.loginlb = QtWidgets.QLabel(self.frame)
        self.loginlb.setGeometry(QtCore.QRect(240, 310, 101, 20))
        self.loginlb.setObjectName("loginlb")
        self.loginlb_2 = QtWidgets.QLabel(self.frame)
        self.loginlb_2.setGeometry(QtCore.QRect(260, 220, 101, 20))
        self.loginlb_2.setObjectName("loginlb_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(-1, -41, 731, 551))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.raise_()
        self.frame.raise_()
        LoginPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 561, 21))
        self.menubar.setObjectName("menubar")
        LoginPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginPage)
        self.statusbar.setObjectName("statusbar")
        LoginPage.setStatusBar(self.statusbar)

        self.retranslateUi(LoginPage)
        QtCore.QMetaObject.connectSlotsByName(LoginPage)

    def retranslateUi(self, LoginPage):
        _translate = QtCore.QCoreApplication.translate
        LoginPage.setWindowTitle(_translate("LoginPage", "MainWindow"))
        self.LoginHere.setText(_translate("LoginPage", "Login Here"))
        self.EnterEmail.setPlaceholderText(_translate("LoginPage", "  Email"))
        self.EnterPassword.setPlaceholderText(_translate("LoginPage", "  Password"))
        self.registerButton.setText(_translate("LoginPage", "Login"))
        self.TermsandConditions.setText(_translate("LoginPage", "I Accept the Terms And Conditions"))
        self.AlreadyAccount.setText(_translate("LoginPage", "Already have an account ?"))
        self.loginlb.setText(_translate("LoginPage", "Forgot Password?"))
        self.loginlb_2.setText(_translate("LoginPage", "Forgot Password?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginPage = QtWidgets.QMainWindow()
    ui = Ui_LoginPage()
    ui.setupUi(LoginPage)
    LoginPage.show()
    sys.exit(app.exec_())
