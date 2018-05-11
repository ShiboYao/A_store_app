from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from database import User
import sys


class Ui_Dialog_update(object):
    def setupUi(self, Dialog, cid):
        Dialog.setObjectName("Update")
        Dialog.setFixedSize(600, 500)
        self.CID = cid
        
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
        
        self.btnupdate = QtWidgets.QPushButton(Dialog)
        self.btnupdate.setGeometry(QtCore.QRect(240, 380, 131, 41))
        self.btnupdate.setObjectName("btnRegister")
        self.btnupdate.clicked.connect(self.updateButton)

        self.label_Heading = QtWidgets.QLabel(Dialog)
        self.label_Heading.setGeometry(QtCore.QRect(120, 30, 431, 61))
        self.label_Heading.setObjectName("label_Heading")
        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        
        
    def retranslateUi(self, Dialog): # ok
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Update"))
        self.label_1.setText(_translate("Dialog", "First Name:"))
        self.label_2.setText(_translate("Dialog", "Last Name:"))
        self.label_3.setText(_translate("Dialog", "Email:"))
        self.label_4.setText(_translate("Dialog", "Address:"))
        self.label_5.setText(_translate("Dialog", "Phone:"))
        self.label_6.setText(_translate("Dialog", "Password:"))
        self.label_7.setText(_translate("Dialog", "Repeat Password:"))
        self.btnupdate.setText(_translate("Dialog", "Update"))
        self.label_Heading.setText(_translate("Dialog", "Update Profile"))
        
        
    def updateButton(self):        
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
                user = User(self.CID)
                r = user.update(fname,lname,email,address, phone, password)
                if r:
                    self.showMessage("Success", "Profile has been updated.")
                    self.clearField()
                else:
                    self.showMessage("Error","Something is wrong.")
   
    def showMessage(self,title,msg):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        #msgBox.setTitle(title)
        msgBox.setText(msg)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()        
        
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



class Ui_Dialog_updateshipadd(object):
    def setupUi(self, Dialog, cid):
        Dialog.setObjectName("Update")
        Dialog.setFixedSize(600, 500)
        self.CID = cid
        
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

        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(110, 360, 161, 21))
        self.label_8.setObjectName("label_7")
                
        self.txtreceiver = QtWidgets.QLineEdit(Dialog)
        self.txtreceiver.setGeometry(QtCore.QRect(290, 150, 151, 21))
        self.txtreceiver.setObjectName("txtreceiver")
        
        self.txtcountry = QtWidgets.QLineEdit(Dialog)
        self.txtcountry.setGeometry(QtCore.QRect(290, 180, 151, 21))
        self.txtcountry.setObjectName("txtcountry")
        
        self.txtstate = QtWidgets.QLineEdit(Dialog)
        self.txtstate.setGeometry(QtCore.QRect(290, 210, 151, 21))
        self.txtstate.setObjectName("txtstate")
        
        self.txtcity = QtWidgets.QLineEdit(Dialog)
        self.txtcity.setGeometry(QtCore.QRect(290, 240, 151, 21))
        self.txtcity.setObjectName("txtcity")
        
        self.txtzip = QtWidgets.QLineEdit(Dialog)
        self.txtzip.setGeometry(QtCore.QRect(290, 270, 151, 21))
        self.txtzip.setObjectName("txtzip")
        
        self.txtstreet = QtWidgets.QLineEdit(Dialog)
        self.txtstreet.setGeometry(QtCore.QRect(290, 300, 151, 21))
        self.txtstreet.setObjectName("txtstreet")
        
        self.txtsnumber = QtWidgets.QLineEdit(Dialog)
        self.txtsnumber.setGeometry(QtCore.QRect(290, 330, 151, 21))
        self.txtsnumber.setObjectName("txtsnumber")

        self.txtsname = QtWidgets.QLineEdit(Dialog)
        self.txtsname.setGeometry(QtCore.QRect(290, 360, 151, 21))
        self.txtsname.setObjectName("txtsname")
                
        self.btnupdate = QtWidgets.QPushButton(Dialog)
        self.btnupdate.setGeometry(QtCore.QRect(240, 400, 131, 41))
        self.btnupdate.setObjectName("btnupdate")
        self.btnupdate.clicked.connect(self.updateButton)

        self.label_Heading = QtWidgets.QLabel(Dialog)
        self.label_Heading.setGeometry(QtCore.QRect(120, 30, 431, 61))
        self.label_Heading.setObjectName("label_Heading")
        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        
        
    def retranslateUi(self, Dialog): # ok
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Ship Address"))
        self.label_1.setText(_translate("Dialog", "Receiver:"))
        self.label_2.setText(_translate("Dialog", "Country:"))
        self.label_3.setText(_translate("Dialog", "State:"))
        self.label_4.setText(_translate("Dialog", "City:"))
        self.label_5.setText(_translate("Dialog", "Zip:"))
        self.label_6.setText(_translate("Dialog", "Street:"))
        self.label_7.setText(_translate("Dialog", "Street number:"))
        self.label_8.setText(_translate("Dialog", "Address name:"))
        self.btnupdate.setText(_translate("Dialog", "Add"))
        self.label_Heading.setText(_translate("Dialog", "Add Ship Address"))
        
        
    def updateButton(self):        
        receiver = self.txtreceiver.text()
        country = self.txtcountry.text()
        state = self.txtstate.text()
        city = self.txtcity.text()
        zipcode = self.txtzip.text()
        street = self.txtstreet.text()
        snumber = self.txtsnumber.text()
        sname = self.txtsname.text()
        if self.checkFields(receiver,country,state, city, zipcode,street,snumber,sname):
            self.showMessage("Error", "All fields must be filled")
        else:
            user = User(self.CID)
            r = user.addinsert(receiver,country,state,city,zipcode,street,snumber,sname)
            if r:
                self.showMessage("Success", "New address is on profile.")
                self.clearField()
            else:
                self.showMessage("Error","Something is wrong.")
   
    def showMessage(self,title,msg):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        #msgBox.setTitle(title)
        msgBox.setText(msg)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()        
        
    def checkFields(self,receiver,country,state, city, zipcode,street,snumber,sname):
        if(receiver=="" or country=="" or state == "" or city == "" or zipcode == "" or street== "" or snumber=="" or sname == ""):
            return True
            
            
    def clearField(self):
        self.txtreceiver.setText(None)
        self.txtcountry.setText(None)
        self.txtstate.setText(None)
        self.txtcity.setText(None)
        self.txtzip.setText(None)
        self.txtstreet.setText(None)
        self.txtsnumber.setText(None)
        self.txtsname.setText(None)
                


class Ui_Dialog_updatecc(object):
    def setupUi(self, Dialog, cid):
        Dialog.setObjectName("Update")
        Dialog.setFixedSize(600, 500)
        self.CID = cid
        
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
                
        self.txtcardnumber = QtWidgets.QLineEdit(Dialog)
        self.txtcardnumber.setGeometry(QtCore.QRect(290, 150, 151, 21))
        self.txtcardnumber.setObjectName("txtcardnumber")
        
        self.txtsecnumber = QtWidgets.QLineEdit(Dialog)
        self.txtsecnumber.setGeometry(QtCore.QRect(290, 180, 151, 21))
        self.txtsecnumber.setObjectName("txtsecnumber")
        
        self.txtowner = QtWidgets.QLineEdit(Dialog)
        self.txtowner.setGeometry(QtCore.QRect(290, 210, 151, 21))
        self.txtowner.setObjectName("txtowner")
        
        self.txttype = QtWidgets.QLineEdit(Dialog)
        self.txttype.setGeometry(QtCore.QRect(290, 240, 151, 21))
        self.txttype.setObjectName("txttype")
        
        self.txtbilling = QtWidgets.QLineEdit(Dialog)
        self.txtbilling.setGeometry(QtCore.QRect(290, 270, 151, 21))
        self.txtbilling.setObjectName("txtbilling")
        
        self.txtexpdate = QtWidgets.QLineEdit(Dialog)
        self.txtexpdate.setGeometry(QtCore.QRect(290, 300, 151, 21))
        self.txtexpdate.setObjectName("txtexpdate")
                
        self.btnupdate = QtWidgets.QPushButton(Dialog)
        self.btnupdate.setGeometry(QtCore.QRect(240, 400, 131, 41))
        self.btnupdate.setObjectName("btnupdate")
        self.btnupdate.clicked.connect(self.updateButton)

        self.label_Heading = QtWidgets.QLabel(Dialog)
        self.label_Heading.setGeometry(QtCore.QRect(120, 30, 431, 61))
        self.label_Heading.setObjectName("label_Heading")
        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        
        
    def retranslateUi(self, Dialog): # ok
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Credit Card"))
        self.label_1.setText(_translate("Dialog", "Card number:"))
        self.label_2.setText(_translate("Dialog", "Security number:"))
        self.label_3.setText(_translate("Dialog", "Owner:"))
        self.label_4.setText(_translate("Dialog", "Type:"))
        self.label_5.setText(_translate("Dialog", "Billing Address:"))
        self.label_6.setText(_translate("Dialog", "Expiration Date:"))
        self.btnupdate.setText(_translate("Dialog", "Add"))
        self.label_Heading.setText(_translate("Dialog", "Add Credit Card"))
        
        
    def updateButton(self):        
        cardnumber = self.txtcardnumber.text()
        secnumber = self.txtsecnumber.text()
        owner = self.txtowner.text()
        cardtype = self.txttype.text()
        billing = self.txtbilling.text()
        expdate = self.txtexpdate.text()

        user = User(self.CID)
        r = user.addcc(cardnumber,secnumber,owner,cardtype,billing,expdate,1)
        if r:
            self.showMessage("Success", "New credit card is on profile.")
            self.clearField()
        else:
            self.showMessage("Error","Something is wrong.")
   
    def showMessage(self,title,msg):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        #msgBox.setTitle(title)
        msgBox.setText(msg)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()        

    def clearField(self):
        self.txtcardnumber.setText(None)
        self.txtsecnumber.setText(None)
        self.txtowner.setText(None)
        self.txttype.setText(None)
        self.txtbilling.setText(None)
        self.txtexpdate.setText(None)
      
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_user()
    ui.setupUi(Dialog, '100000003')

    Dialog.show()


    sys.exit(app.exec_())   
    
    
    
    
    
    
    
    
    
