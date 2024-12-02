# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets # type: ignore
import sqlite3

class Ui_CompleteScanDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(469, 438)
        
        Dialog.setWindowIcon(QtGui.QIcon("C:/Users/sevim/Desktop/antivirus/qt/icons/flag.png"))
        Dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        
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
        Dialog.setWindowTitle(_translate("Dialog", "Complete Scan"))
        self.label_2.setText(_translate("Dialog", "COMPLETE SCAN"))
        self.label.setText(_translate("Dialog", "Your C disk will be scanned. This may take some time."))
        self.complete_scan_pushButton.setText(_translate("Dialog", "Start Scanning"))
        self.label_3.setText(_translate("Dialog", "Scan Results:"))

class a_complete_scan_dialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(a_complete_scan_dialog, self).__init__(parent)
        self.ui = Ui_CompleteScanDialog()
        self.ui.setupUi(self)

        self.ui.complete_scan_pushButton.clicked.connect(self.start_scan)

    def start_scan(self):
        try:
            conn1 = sqlite3.connect("c_hashes.db")
            c1 = conn1.cursor()
            conn2 = sqlite3.connect("updated_virus_hashes.db")
            c2 = conn2.cursor()

            c1.execute("SELECT file_path, hash_value FROM hashes")
            dosya_bil = c1.fetchall()
            c2.execute("SELECT current_virus_hash FROM sha256_hashes")
            virus_bil = c2.fetchall()

            set1 = set(dosya_bil)
            set2 = set(virus_bil)

            #   eksik ya da yanlis indirilmis/bozuk dosyalarin ortak hashi
            skip_this_hashes = {"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"}

            #   ortak veriler yani virusler
            common_datas = set((file_path, hash_value) for file_path, hash_value in dosya_bil if (hash_value,) in set2)

            self.ui.complete_scan_result_plainTextEdit.clear()

            QtWidgets.QMessageBox.information(self, "successful!", "scan is completed!")

            common_files = []
            for file_path, hash_value in dosya_bil:
                try:
                    if hash_value in common_datas and hash_value not in skip_this_hashes:
                        common_files.append((file_path, hash_value))
                except Exception as e:
                    print(f"skipping file {file_path} due to error: {e}")

            if common_files:
                self.ui.complete_scan_result_plainTextEdit.appendPlainText("Virus detected!\nDetected virus hashes:\n")
                for file_path, hash_value in common_files:
                    self.ui.complete_scan_result_plainTextEdit.appendPlainText(f"->File: {file_path}\n->Hash: {hash_value}\n")
            else:
                self.ui.complete_scan_result_plainTextEdit.appendPlainText("scan is clean.")

            conn1.close()
            conn2.close()

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "error", f"an error occurred: {e}")

#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    dialog = a_complete_scan_dialog()
#    dialog.show()
#    sys.exit(app.exec_())
