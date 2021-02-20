def messagebox(self, title, message):
    mess = QtWidgets.QMessageBox( )
    mess.setWindowTitle( title )
    mess.setText( message )
    mess.setStandardButtons( QtWidgets.QMessageBox.Ok )
    mess.exec_( )


def update(self):
    email = self.lineEdit.text( )
    password = self.lineEdit_2.text( )
    old = self.lineEdit_3.text( )
    con = pymysql.connect( host="localhost", port=3306, user="root", password="", db="dumb_can_speak" )
    cur = con.cursor( )
    with open( "login-detail.txt", "r" ) as file:  # wirting user id into a file
        userId = file.read( )
        print( userId );
    query = "Select * from users Where userId=%s And password=%s"
    data = cur.execute( query, (userId, password) )
    get = cur.fetchone( )
    if old != '' and email != '' and password != '':
        if len( get ) > 0:
            query2 = "UPDATE `users` SET `password`=%s WHERE userId=%s"
            data = cur.execute( query2, (password, userId) )
            con.commit( )  # finalize the changes
            # Close the connection
            cur.close( )
            con.close( )
            if (data):
                self.messagebox( "Congrats", "Your profile updated" )
            else:
                self.messagebox( "Alert", "Sorry Something went wrong try again" )
        else:
            self.messagebox( "Alert", "Password does not match" )
    else:
        self.messagebox( "Alert", "Please fill all the required fields" )



    if __name__ == "__main__":
        import sys

        app = QtWidgets.QApplication( sys.argv )
        MainWindow = QtWidgets.QMainWindow( )
        ui = Ui_Profile( )
        ui.setupProfileUi( MainWindow )
        MainWindow.show( )
        sys.exit( app.exec_( ) )