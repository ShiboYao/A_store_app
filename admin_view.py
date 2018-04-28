from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from database import Admin, tupleMsg
import sys

class Ui_Dialog_admin(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Admin")
        Dialog.setFixedSize(600, 400)
        
        self.label1 = QtWidgets.QLabel(Dialog)
        self.label1.setGeometry(QtCore.QRect(260, 110, 191, 27))
        self.label1.setObjectName("label1")
        
        self.txtdate1 = QtWidgets.QLineEdit(Dialog)
        self.txtdate1.setGeometry(QtCore.QRect(300, 110, 151, 21))
        self.txtdate1.setObjectName("date1")
        
        self.label2 = QtWidgets.QLabel(Dialog)
        self.label2.setGeometry(QtCore.QRect(260, 160, 191, 27))
        self.label2.setObjectName("label2")
        
        self.txtdate2 = QtWidgets.QLineEdit(Dialog)
        self.txtdate2.setGeometry(QtCore.QRect(300, 160, 151, 21))
        self.txtdate2.setObjectName("date2")


        self.r1 = QtWidgets.QRadioButton(Dialog)
        self.r1.setObjectName("r1")
        self.r1.condition = "Sold by Quant"
        self.r1.clicked.connect(self.on_radio_button_clicked)
        self.r1.setGeometry(QtCore.QRect(20, 80, 151, 21))

        self.r2 = QtWidgets.QRadioButton(Dialog)
        self.r2.setObjectName("r2")
        self.r2.condition = "Sold by Customer"
        self.r2.clicked.connect(self.on_radio_button_clicked)
        self.r2.setGeometry(QtCore.QRect(20, 120, 151, 21))

        self.r3 = QtWidgets.QRadioButton(Dialog)
        self.r3.setObjectName("r3")
        self.r3.condition = "Ten Customer"
        self.r3.clicked.connect(self.on_radio_button_clicked)
        self.r3.setGeometry(QtCore.QRect(20, 160, 151, 21))

        self.r4 = QtWidgets.QRadioButton(Dialog)
        self.r4.setObjectName("r4")
        self.r4.condition = "Five Zip"
        self.r4.clicked.connect(self.on_radio_button_clicked)
        self.r4.setGeometry(QtCore.QRect(20, 200, 151, 21))
        
        self.r5 = QtWidgets.QRadioButton(Dialog)
        self.r5.setObjectName("r5")
        self.r5.condition = "Average Price"
        self.r5.clicked.connect(self.on_radio_button_clicked)
        self.r5.setGeometry(QtCore.QRect(20, 240, 151, 21))

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(300, 260, 100, 20))
        self.label.setObjectName("label")
        
        self.txtview = QtWidgets.QLineEdit(Dialog)
        self.txtview.setGeometry(QtCore.QRect(360, 260, 100, 20))
        self.txtview.setObjectName("view")

        self.labelnew = QtWidgets.QLabel(Dialog)
        self.labelnew.setGeometry(QtCore.QRect(180, 300, 100, 20))
        self.labelnew.setObjectName("labelnew")
        
        self.txtnew = QtWidgets.QLineEdit(Dialog)
        self.txtnew.setGeometry(QtCore.QRect(260, 300, 30, 20))
        self.txtnew.setObjectName("new")
                
        self.btnlookup = QtWidgets.QPushButton(Dialog)
        self.btnlookup.setGeometry(QtCore.QRect(460, 260, 80, 20))
        self.btnlookup.setObjectName("btnlookup")
        self.btnlookup.clicked.connect(self.lookupButton)

        self.labelprocess = QtWidgets.QLabel(Dialog)
        self.labelprocess.setGeometry(QtCore.QRect(300, 300, 100, 20))
        self.labelprocess.setObjectName("labelprocess")
        
        self.txtprocess = QtWidgets.QLineEdit(Dialog)
        self.txtprocess.setGeometry(QtCore.QRect(360, 300, 100, 20))
        self.txtprocess.setObjectName("process")        

        self.btnprocess = QtWidgets.QPushButton(Dialog)
        self.btnprocess.setGeometry(QtCore.QRect(460, 300, 80, 20))
        self.btnprocess.setObjectName("btnprocess")
        self.btnprocess.clicked.connect(self.processButton)
                
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

       
    def retranslateUi(self, Dialog): # ok
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Admin"))
        self.label1.setText(_translate("Dialog", "Date1:"))
        self.label2.setText(_translate("Dialog", "Date2:"))
        self.r1.setText(_translate("Dialog", "Sold by Quant"))
        self.r2.setText(_translate("Dialog", "Sold by Customer"))
        self.r3.setText(_translate("Dialog", "Ten Customer"))
        self.r4.setText(_translate("Dialog", "Five Zip"))
        self.r5.setText(_translate("Dialog", "Average Price"))       
        self.labelprocess.setText(_translate("Dialog", "Order No.:"))         
        self.label.setText(_translate("Dialog", "Status:"))         
        self.labelnew.setText(_translate("Dialog", "New Status:"))                 
        self.btnprocess.setText(_translate("Dialog", "Process"))
        self.btnlookup.setText(_translate("Dialog", "Look up"))

    def lookupButton(self):
        status = self.txtview.text()
        admin = Admin()
        r = admin.viewbystatus(status)     
        self.showMessage(tupleMsg(r))

    def processButton(self):
        ordernum = self.txtprocess.text()
        status = self.txtnew.text()
        admin = Admin()
        r = admin.processorder(ordernum, status)   
        if r:  
            self.showMessage("Order processed.")
        else:
            self.showMessage("Failed to process.")    
            
    def on_radio_button_clicked(self):
        Administration = Admin()
        date1 = self.txtdate1.text()
        date2 = self.txtdate2.text()
                
        if self.r1.isChecked():
            r = Administration.mostsold(date1, date2)
        elif self.r2.isChecked():
            r = Administration.mostsold2(date1, date2)
        elif self.r3.isChecked():
            r = Administration.ten_customer(date1, date2)
        elif self.r4.isChecked():
            r = Administration.five_zip(date1, date2)
        elif self.r5.isChecked():
            r = Administration.avg_price(date1, date2)

        msg = tupleMsg(r)
        self.showMessage(msg)
            
    
    def showMessage(self, msg):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText(msg)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
       

        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_admin()
    ui.setupUi(Dialog)

    Dialog.show()


    sys.exit(app.exec_())





