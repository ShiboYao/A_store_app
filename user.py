from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from database import Sign, User, tupleMsg #importing database.py
from shop import Ui_Dialog_shop
from profile import Ui_Dialog_update, Ui_Dialog_updatecc, Ui_Dialog_updateshipadd
import sys


class Ui_Dialog_user(object):
    def setupUi(self, Dialog, cid):
        Dialog.setObjectName("User Center")
        Dialog.setFixedSize(600, 350)
        self.CID = cid


        self.r11 = QtWidgets.QRadioButton(Dialog)
        self.r11.setObjectName("r1")
        self.r11.condition = "View Credit Card"
        self.r11.clicked.connect(self.on_radio_button_clicked)
        self.r11.setGeometry(QtCore.QRect(20, 0, 151, 21))

        self.btnupdatecc = QtWidgets.QPushButton(Dialog)
        self.btnupdatecc.setGeometry(QtCore.QRect(300, 0, 151, 21))
        self.btnupdatecc.setObjectName("Add Credit Card")
        self.btnupdatecc.clicked.connect(self.addccButton)  
        
        self.r12 = QtWidgets.QRadioButton(Dialog)
        self.r12.setObjectName("r1")
        self.r12.condition = "View Ship Address"
        self.r12.clicked.connect(self.on_radio_button_clicked)
        self.r12.setGeometry(QtCore.QRect(20, 40, 151, 21))

        self.btnupdateshipadd = QtWidgets.QPushButton(Dialog)
        self.btnupdateshipadd.setGeometry(QtCore.QRect(300, 40, 151, 21))
        self.btnupdateshipadd.setObjectName("Add Ship Address")
        self.btnupdateshipadd.clicked.connect(self.addshipaddButton)                  
        
        self.r1 = QtWidgets.QRadioButton(Dialog)
        self.r1.setObjectName("r1")
        self.r1.condition = "View Profile"
        self.r1.clicked.connect(self.on_radio_button_clicked)
        self.r1.setGeometry(QtCore.QRect(20, 80, 151, 21))

        self.btnupdate = QtWidgets.QPushButton(Dialog)
        self.btnupdate.setGeometry(QtCore.QRect(300, 80, 151, 21))
        self.btnupdate.setObjectName("Update")
        self.btnupdate.clicked.connect(self.updateButton)  
        
        self.r2 = QtWidgets.QRadioButton(Dialog)
        self.r2.setObjectName("r2")
        self.r2.condition = "View History"
        self.r2.clicked.connect(self.on_radio_button_clicked)
        self.r2.setGeometry(QtCore.QRect(20, 120, 151, 21))

        self.btnshop = QtWidgets.QPushButton(Dialog)
        self.btnshop.setGeometry(QtCore.QRect(300, 120, 151, 21))
        self.btnshop.setObjectName("Shop")
        self.btnshop.clicked.connect(self.shopButton)  
        
        self.r3 = QtWidgets.QRadioButton(Dialog)
        self.r3.setObjectName("r3")
        self.r3.condition = "View by Pname"
        self.r3.clicked.connect(self.on_radio_button_clicked)
        self.r3.setGeometry(QtCore.QRect(20, 160, 151, 21))
        
        self.txtpname = QtWidgets.QLineEdit(Dialog)
        self.txtpname.setGeometry(QtCore.QRect(300, 160, 151, 21))
        self.txtpname.setObjectName("pname")

        self.r4 = QtWidgets.QRadioButton(Dialog)
        self.r4.setObjectName("r4")
        self.r4.condition = "View by Ptype"
        self.r4.clicked.connect(self.on_radio_button_clicked)
        self.r4.setGeometry(QtCore.QRect(20, 200, 151, 21))

        self.txtptype = QtWidgets.QLineEdit(Dialog)
        self.txtptype.setGeometry(QtCore.QRect(300, 200, 151, 21))
        self.txtptype.setObjectName("ptype")
                
        self.r5 = QtWidgets.QRadioButton(Dialog)
        self.r5.setObjectName("r5")
        self.r5.condition = "View by Status"
        self.r5.clicked.connect(self.on_radio_button_clicked)
        self.r5.setGeometry(QtCore.QRect(20, 240, 151, 21))
        
        self.txtstatus = QtWidgets.QLineEdit(Dialog)
        self.txtstatus.setGeometry(QtCore.QRect(300, 240, 151, 21))
        self.txtstatus.setObjectName("status")        
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)        
        
        
    def retranslateUi(self, Dialog): # ok
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Customer Center"))
        self.r11.setText(_translate("Dialog", "View Credit Card"))
        self.r12.setText(_translate("Dialog", "view Ship Address"))
        self.r1.setText(_translate("Dialog", "View Profile"))
        self.r2.setText(_translate("Dialog", "View History"))
        self.r3.setText(_translate("Dialog", "View by Pname"))
        self.r4.setText(_translate("Dialog", "View by Ptype"))
        self.r5.setText(_translate("Dialog", "View by Status"))        
        self.btnshop.setText(_translate("Dialog", "Shop"))
        self.btnupdate.setText(_translate("Dialog", "Update Profile"))
        self.btnupdatecc.setText(_translate("Dialog", "Add Credit Card"))
        self.btnupdateshipadd.setText(_translate("Dialog", "Add Ship Address"))

        
    def shopButton(self):   
        self.shopDialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog_shop()
        self.ui.setupUi(self.shopDialog, self.CID)
        self.shopDialog.show()       
        
    def updateButton(self):   
        self.updateDialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog_update()
        self.ui.setupUi(self.updateDialog, self.CID)
        self.updateDialog.show()   
        
    def addccButton(self):   
        self.updateDialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog_updatecc()
        self.ui.setupUi(self.updateDialog, self.CID)
        self.updateDialog.show()   
        
    def addshipaddButton(self):   
        self.updateDialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog_updateshipadd()
        self.ui.setupUi(self.updateDialog, self.CID)
        self.updateDialog.show()   
        
    def on_radio_button_clicked(self):
        User_view = User(self.CID)
        pname = self.txtpname.text()
        ptype = self.txtptype.text()
        status = self.txtstatus.text()      
        
        if self.r11.isChecked():
            r = User_view.ccoption()
        elif self.r12.isChecked():
            r = User_view.addoption()        
        elif self.r1.isChecked():
            r = User_view.viewprofile()
        elif self.r2.isChecked():
            r = User_view.viewhistory()
        elif self.r3.isChecked():
            r = User_view.viewbypname(pname)
        elif self.r4.isChecked():
            r = User_view.viewbyptype(ptype)
        elif self.r5.isChecked():
            r = User_view.viewbystatus(status)

        msg = tupleMsg(r)
        print(msg)
        self.showMessage(msg)
        
        
    def showMessage(self, msg):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setFixedSize(597, 356)
        msgBox.setText(msg)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_user()
    ui.setupUi(Dialog, '100000003')

    Dialog.show()


    sys.exit(app.exec_())        
                
                
