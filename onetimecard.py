from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from database import Cart, User, tupleMsg
import sys


class Ui_Dialog_updatecc(object):
    def setupUi(self, Dialog, cid):
        Dialog.setObjectName("One Time Payment")
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
        
        
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(250, 80, 80, 30))
        self.label_7.setObjectName("Ship Address")

        self.txtship = QtWidgets.QLineEdit(Dialog)
        self.txtship.setGeometry(QtCore.QRect(340, 80, 100, 30))
        self.txtship.setObjectName("txtqship")

        self.btnviewshipadd = QtWidgets.QPushButton(Dialog)
        self.btnviewshipadd.setGeometry(QtCore.QRect(460, 80, 120, 30))
        self.btnviewshipadd.setObjectName("btnviewshipadd")
        self.btnviewshipadd.clicked.connect(self.viewshipaddButton)
        
                        
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
        Dialog.setWindowTitle(_translate("Dialog", "One Time Payment"))
        self.label_1.setText(_translate("Dialog", "Card number:"))
        self.label_2.setText(_translate("Dialog", "Security number:"))
        self.label_3.setText(_translate("Dialog", "Owner:"))
        self.label_4.setText(_translate("Dialog", "Type:"))
        self.label_5.setText(_translate("Dialog", "Billing Address:"))
        self.label_6.setText(_translate("Dialog", "Expiration Date:"))
        self.label_7.setText(_translate("Dialog", "Ship Address:"))
        self.btnviewshipadd.setText(_translate("Dialog", "View ShipAdd"))
        self.btnupdate.setText(_translate("Dialog", "Checkout"))
        self.label_Heading.setText(_translate("Dialog", "One Time Payment"))


        
    def viewshipaddButton(self):
        cart = Cart(self.CID)
        r = cart.addoption()     
        self.showMessage("Shipping", tupleMsg(r))         
        
    def updateButton(self):        
        cardnumber = self.txtcardnumber.text()
        secnumber = self.txtsecnumber.text()
        owner = self.txtowner.text()
        cardtype = self.txttype.text()
        billing = self.txtbilling.text()
        expdate = self.txtexpdate.text()

        user = User(self.CID)
        r = user.addcc(cardnumber,secnumber,owner,cardtype,billing,expdate,0)
        if r:
            addname = self.txtship.text()
            ccnumber = self.txtcardnumber.text()
            cart = Cart(self.CID)
            s = cart.checkout(addname, ccnumber)
            if s == True:
                self.showMessage("Transaction", "Order placed.")
                self.clearField()
        else:
            self.showMessage("Error","Card was already on file.")
   
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
    ui = Ui_Dialog_updatecc()
    ui.setupUi(Dialog, '100000003')

    Dialog.show()


    sys.exit(app.exec_())   
