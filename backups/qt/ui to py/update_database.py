# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_database.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(510, 508)
        Dialog.setStyleSheet("QDialog\n"
"{\n"
"    background-image: url(C:/Users/sevim/Desktop/antivirus/qt/icons/3.webp);\n"
"}")
        self.update_pushButton = QtWidgets.QPushButton(Dialog)
        self.update_pushButton.setGeometry(QtCore.QRect(260, 160, 231, 31))
        self.update_pushButton.setStyleSheet("font: 8pt \"8514oem\";")
        self.update_pushButton.setObjectName("update_pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 471, 21))
        self.label.setStyleSheet("font: 63 7pt \"Yu Gothic UI Semibold\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(190, 30, 531, 21))
        self.label_2.setStyleSheet("font: 63 7pt \"Yu Gothic UI Semibold\";")
        self.label_2.setObjectName("label_2")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(260, 450, 226, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("font: 63 8pt \"Yu Gothic UI Semibold\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.update_dateTimeEdit = QtWidgets.QDateTimeEdit(self.layoutWidget)
        self.update_dateTimeEdit.setStyleSheet("font: 63 7pt \"Yu Gothic UI Semibold\";\n"
"border: none;")
        self.update_dateTimeEdit.setObjectName("update_dateTimeEdit")
        self.horizontalLayout.addWidget(self.update_dateTimeEdit)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.update_pushButton.setText(_translate("Dialog", "Update Database"))
        self.label.setText(_translate("Dialog", "warning! a robot test must be passed when accessing the site where updates are received."))
        self.label_2.setText(_translate("Dialog", "please do the test correctly!"))
        self.label_3.setText(_translate("Dialog", "Last Updated:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
