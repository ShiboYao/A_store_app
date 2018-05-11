from PyQt5 import QtCore, QtGui, QtWidgets
from database import Sign


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Sign Up")
        Dialog.setFixedSize(640, 440)


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

        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)

        self.txtPassword.setGeometry(QtCore.QRect(290, 300, 151, 21))
        self.txtPassword.setObjectName("txtPassword")
        
        self.txtPassword2 = QtWidgets.QLineEdit(Dialog)

        self.txtPassword2.setEchoMode(QtWidgets.QLineEdit.Password)

        self.txtPassword2.setGeometry(QtCore.QRect(290, 330, 151, 21))
        self.txtPassword2.setObjectName("txtPassword2")
        
        self.btnRegister = QtWidgets.QPushButton(Dialog)
        self.btnRegister.setGeometry(QtCore.QRect(240, 380, 131, 41))
        self.btnRegister.setObjectName("btnRegister")

        self.btnRegister.clicked.connect(self.registerButton)

        self.label_Heading = QtWidgets.QLabel(Dialog)
        self.label_Heading.setGeometry(QtCore.QRect(120, 30, 431, 61))
        self.label_Heading.setObjectName("label_Heading")
        

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
                new_cid = Registration.signup(fname,lname,email,address, phone, password)
                if new_cid != False:
                    self.showMessage("Success","CID:"+new_cid)
                    self.clearField()
                else:
                    self.showMessage("Error","Something is wrong.")
       
    def showMessage(self,title,msg):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)

        msgBox.setText(msg)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sign Up"))
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
        


    def checkPassword(self,password1, password2):
        return password1 == password2


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

