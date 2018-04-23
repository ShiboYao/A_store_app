from PyQt5 import QtCore, QtGui, QtWidgets
from database import Sign


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(638, 441)
        Dialog.setStyleSheet("QDialog{background-color:\n"
"\n"
"qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0))}\n"
"\n"
"QLineEdit{\n"
"background-color:rgb(170, 255, 127)\n"
"\n"
"}\n"
"\n"
"QLabel#label_Heading{\n"
"font: 75 25pt \"Century Schoolbook L\";\n"
"\n"
"}\n"
"\n"
"\n"
"QLabel{\n"
"font: 75 italic 14pt \"Century Schoolbook L\";\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color:qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));\n"
"color:rgb(255, 255, 255)\n"
"}\n"
"")
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(110, 150, 180, 21))
        self.label_1.setObjectName("label1")
        
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 180, 151, 21))
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(110, 210, 151, 21))
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(110, 240, 151, 21))
        self.label_4.setObjectName("label_4")
        
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(110, 270, 151, 21))
        self.label_5.setObjectName("label_5")
        
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(110, 300, 151, 21))
        self.label_6.setObjectName("label_6")
        
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(110, 330, 161, 21))
        self.label_7.setObjectName("label_7")
        
        self.txtfname = QtWidgets.QLineEdit(Dialog)
        self.txtfname.setGeometry(QtCore.QRect(290, 150, 151, 21))
        self.txtfname.setObjectName("txtfname")
        
        self.txtlname = QtWidgets.QLineEdit(Dialog)
        self.txtlname.setGeometry(QtCore.QRect(290, 180, 151, 21))
        self.txtlname.setObjectName("txtlname")
        
        self.txtemail = QtWidgets.QLineEdit(Dialog)
        self.txtemail.setGeometry(QtCore.QRect(290, 210, 151, 21))
        self.txtemail.setObjectName("txtemail")
        
        self.txtaddress = QtWidgets.QLineEdit(Dialog)
        self.txtaddress.setGeometry(QtCore.QRect(290, 240, 151, 21))
        self.txtaddress.setObjectName("txtaddress")
        
        self.txtphone = QtWidgets.QLineEdit(Dialog)
        self.txtphone.setGeometry(QtCore.QRect(290, 270, 151, 21))
        self.txtphone.setObjectName("txtphone")
        
        self.txtPassword = QtWidgets.QLineEdit(Dialog)
        ################## make the password invisible ############
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        ###########################################################
        self.txtPassword.setGeometry(QtCore.QRect(290, 300, 151, 21))
        self.txtPassword.setObjectName("txtPassword")
        
        self.txtPassword2 = QtWidgets.QLineEdit(Dialog)
        ################## make the password2 invisible ############
        self.txtPassword2.setEchoMode(QtWidgets.QLineEdit.Password)
        ###########################################################
        self.txtPassword2.setGeometry(QtCore.QRect(290, 330, 151, 21))
        self.txtPassword2.setObjectName("txtPassword2")
        
        self.btnRegister = QtWidgets.QPushButton(Dialog)
        self.btnRegister.setGeometry(QtCore.QRect(240, 380, 131, 41))
        self.btnRegister.setObjectName("btnRegister")
        ################## register button#########################
        self.btnRegister.clicked.connect(self.registerButton)
        ###########################################################
        self.label_Heading = QtWidgets.QLabel(Dialog)
        self.label_Heading.setGeometry(QtCore.QRect(120, 30, 431, 61))
        self.label_Heading.setObjectName("label_Heading")
        
        '''

        
        self.txtName = QtWidgets.QLineEdit(Dialog)
        self.txtName.setGeometry(QtCore.QRect(290, 150, 221, 27))
        self.txtName.setObjectName("txtName")
        '''
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def registerButton(self):
        fname = self.txtfname.text()
        lname = self.txtlname.text()
        email = self.txtemail.text()
        address = self.txtaddress.text()
        phone = self.txtphone.text()
        password = self.txtPassword.text()
        password2 = self.txtPassword2.text()
        if self.checkFields(fname,lname,email,address, phone,password):
            self.showMessage("Error", "All fields must be filled")
        else:
            if(self.checkPassword(password,password2)):
                Registration = Sign()
                Registration.signup(fname,lname,email,address, phone, password)
                self.showMessage("Success","Registration successul")
                self.clearField()
            else:
                self.showMessage("Error","Passwords doesn't match")
       
    def showMessage(self,title,msg):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        #msgBox.setTitle(title)
        msgBox.setText(msg)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_1.setText(_translate("Dialog", "First Name:"))
        self.label_2.setText(_translate("Dialog", "Last Name:"))
        self.label_3.setText(_translate("Dialog", "Email:"))
        self.label_4.setText(_translate("Dialog", "Address:"))
        self.label_5.setText(_translate("Dialog", "Phone:"))
        self.label_6.setText(_translate("Dialog", "Password:"))
        self.label_7.setText(_translate("Dialog", "Repeat Password:"))
        self.btnRegister.setText(_translate("Dialog", "Register"))
        self.label_Heading.setText(_translate("Dialog", "Create Account"))
        

    def loginPage(self):
        self.loginWindow = QtWidgets.QDialog()
        self.ui = Ui_Dialog2()
        self.ui.setupUi(self.loginWindow)
        self.loginWindow.show()
        
    def checkFields(self,fname,lname,email,address,phone,password):
        if(fname=="" or lname=="" or email == "" or address == "" or phone == "" or password== ""):
            return True
        

    ############## check if password1 and password2 matches #############
    def checkPassword(self,password1, password2):
        return password1 == password2

    ##################### clear fields ##################
    def clearField(self):
        self.txtfname.setText(None)
        self.txtlname.setText(None)
        self.txtemail.setText(None)
        self.txtaddress.setText(None)
        self.txtphone.setText(None)
        self.txtPassword.setText(None)
        self.txtPassword2.setText(None)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

