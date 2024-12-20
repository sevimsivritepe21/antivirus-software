# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'complete_scan.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(469, 438)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setStyleSheet("font: 8pt \"8514oem\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setStyleSheet("font: 63 9pt \"Yu Gothic UI Semibold\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.complete_scan_pushButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.complete_scan_pushButton.sizePolicy().hasHeightForWidth())
        self.complete_scan_pushButton.setSizePolicy(sizePolicy)
        self.complete_scan_pushButton.setStyleSheet("font: 8pt \"8514oem\";")
        self.complete_scan_pushButton.setObjectName("complete_scan_pushButton")
        self.verticalLayout.addWidget(self.complete_scan_pushButton)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setStyleSheet("font: 63 9pt \"Yu Gothic UI Semibold\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.complete_scan_result_plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.complete_scan_result_plainTextEdit.setObjectName("complete_scan_result_plainTextEdit")
        self.verticalLayout_2.addWidget(self.complete_scan_result_plainTextEdit)
        spacerItem3 = QtWidgets.QSpacerItem(30, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "COMPLETE SCAN"))
        self.label.setText(_translate("Dialog", "your c disc will be scanned. this may take some time."))
        self.complete_scan_pushButton.setText(_translate("Dialog", "start scanning"))
        self.label_3.setText(_translate("Dialog", "scan results:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
