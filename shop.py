from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from database import Cart, tupleMsg
import sys


class Ui_Dialog_shop(object):
    def setupUi(self, Dialog, cid):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(600, 400)
        self.CID = cid

        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(20, 150, 80, 30))
        self.label_1.setObjectName("ProductID")
        
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 180, 80, 30))
        self.label_2.setObjectName("Quant")

        self.txtPID = QtWidgets.QLineEdit(Dialog)
        self.txtPID.setGeometry(QtCore.QRect(100, 150, 100, 30))
        self.txtPID.setObjectName("txtPID")
        
        self.txtquant = QtWidgets.QLineEdit(Dialog)
        self.txtquant.setGeometry(QtCore.QRect(100, 180, 100, 30))
        self.txtquant.setObjectName("txtquant")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(250, 150, 80, 30))
        self.label_3.setObjectName("Payment:")
        
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(250, 180, 80, 30))
        self.label_4.setObjectName("Ship Address")

        self.txtpayment = QtWidgets.QLineEdit(Dialog)
        self.txtpayment.setGeometry(QtCore.QRect(340, 150, 100, 30))
        self.txtpayment.setObjectName("txtpayment")
        
        self.txtship = QtWidgets.QLineEdit(Dialog)
        self.txtship.setGeometry(QtCore.QRect(340, 180, 100, 30))
        self.txtship.setObjectName("txtqship")
        
        self.combobox = QComboBox(Dialog)
        self.combobox.setGeometry(QtCore.QRect(20, 20, 100, 40))
        self.combobox.setObjectName("View Product")
        self.combobox.addItem("")
        self.combobox.addItem("")
        self.combobox.addItem("")
        self.combobox.addItem("")
        
        self.btnview = QtWidgets.QPushButton(Dialog)
        self.btnview.setGeometry(QtCore.QRect(20, 80, 50, 20))
        self.btnview.setObjectName("btnView")
        self.btnview.clicked.connect(self.viewButton)

        self.btnadd = QtWidgets.QPushButton(Dialog)
        self.btnadd.setGeometry(QtCore.QRect(20, 220, 60, 20))
        self.btnadd.setObjectName("btnAdd")
        self.btnadd.clicked.connect(self.addButton)
        
        self.btnremove = QtWidgets.QPushButton(Dialog)
        self.btnremove.setGeometry(QtCore.QRect(100, 220, 60, 20))
        self.btnremove.setObjectName("btnRemove")
        self.btnremove.clicked.connect(self.removeButton)
        
        self.btnviewcart = QtWidgets.QPushButton(Dialog)
        self.btnviewcart.setGeometry(QtCore.QRect(20, 260, 120, 20))
        self.btnviewcart.setObjectName("btnViewcart")
        self.btnviewcart.clicked.connect(self.viewcartButton)
        
        self.btnviewpay = QtWidgets.QPushButton(Dialog)
        self.btnviewpay.setGeometry(QtCore.QRect(460, 150, 120, 30))
        self.btnviewpay.setObjectName("btnviewpay")
        self.btnviewpay.clicked.connect(self.viewpayButton)
        
        self.btnviewshipadd = QtWidgets.QPushButton(Dialog)
        self.btnviewshipadd.setGeometry(QtCore.QRect(460, 180, 120, 30))
        self.btnviewshipadd.setObjectName("btnviewshipadd")
        self.btnviewshipadd.clicked.connect(self.viewshipaddButton)

        self.btncheckout = QtWidgets.QPushButton(Dialog)
        self.btncheckout.setGeometry(QtCore.QRect(460, 300, 120, 30))
        self.btncheckout.setObjectName("btncheckout")
        self.btncheckout.clicked.connect(self.checkoutButton)
                
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def retranslateUi(self, Dialog): # ok
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

        self.label_1.setText(_translate("Dialog", "ProductID:"))
        self.label_2.setText(_translate("Dialog", "Quant:"))        
        self.label_3.setText(_translate("Dialog", "Payment:"))
        self.label_4.setText(_translate("Dialog", "Ship Address:"))           
        
        self.combobox.setItemText(0, _translate("Dialog", "Printer"))
        self.combobox.setItemText(1, _translate("Dialog", "Laptop"))
        self.combobox.setItemText(2, _translate("Dialog", "Desktop"))
        self.combobox.setItemText(3, _translate("Dialog", "All"))
        self.btnview.setText(_translate("Dialog", "View"))
        self.btnadd.setText(_translate("Dialog", "Add"))
        self.btnremove.setText(_translate("Dialog", "Remove"))
        self.btnviewcart.setText(_translate("Dialog", "View Cart"))
        self.btnviewpay.setText(_translate("Dialog", "View Payment"))
        self.btnviewshipadd.setText(_translate("Dialog", "View ShipAdd"))
        self.btncheckout.setText(_translate("Dialog", "Check Out"))
        
                                        
        
    def viewButton(self):
        ptype = self.combobox.currentText()
        cart = Cart(self.CID)
        r = cart.viewbytype(ptype)     
        self.showMessage(ptype, tupleMsg(r))
    
    def addButton(self):
        pid = self.txtPID.text()
        quant = self.txtquant.text()
        cart = Cart(self.CID)
        r = cart.addproduct(pid, quant)     
        if r:
            self.showMessage("Success", "Product added.\n")
        else:
            self.showMessage("Failed", "Wrong Product ID or product already exist in cart.\n")
        
    def removeButton(self):
        pid = self.txtPID.text()
        quant = self.txtquant.text()
        cart = Cart(self.CID)
        r = cart.deleteproduct(pid)     
        if r:
            self.showMessage("Success", "Product removed.\n")
        else:
            self.showMessage("Failed", "Wrong Product ID or product doesn't exist in cart.\n")

    def viewcartButton(self):
        cart = Cart(self.CID)
        r = cart.view()     
        self.showMessage("Cart", tupleMsg(r))


    def viewpayButton(self):
        cart = Cart(self.CID)
        r = cart.ccoption()     
        self.showMessage("Payment", tupleMsg(r))
        
    def viewshipaddButton(self):
        cart = Cart(self.CID)
        r = cart.addoption()     
        self.showMessage("Shipping", tupleMsg(r))        

    def checkoutButton(self):
        ccnumber = self.txtpayment.text()
        addname = self.txtship.text()
        cart = Cart(self.CID)
        r = cart.checkout(addname, ccnumber)
        if r == True:
            self.showMessage("Transaction", "Order Placed.")   
        
                      
    def showMessage(self,title,msg):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        #msgBox.setTitle(title)
        msgBox.setText(msg)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()    
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_shop()
    ui.setupUi(Dialog, '100000003')

    Dialog.show()
    


    sys.exit(app.exec_())   
    
    
    
    
    
    
    
    
    
