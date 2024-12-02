# -*- coding: utf-8 -*-
import sqlite3
import os

from PyQt5 import QtCore, QtGui, QtWidgets # type: ignore


class Ui_CleaningDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(551, 568)

        #pencereye icon ekleyelim
        Dialog.setWindowIcon(QtGui.QIcon("/icons/clean.png")) 

        #flags
        Dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("QFrame \n"
"{    background-image: url(C:/Users/sevim/Desktop/antivirus/qt/icons/1.webp);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout.addWidget(self.frame)
        spacerItem = QtWidgets.QSpacerItem(25, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.cleaning_progressBar = QtWidgets.QProgressBar(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cleaning_progressBar.sizePolicy().hasHeightForWidth())
        self.cleaning_progressBar.setSizePolicy(sizePolicy)
        self.cleaning_progressBar.setStyleSheet("font: 63 8pt \"Yu Gothic UI Semibold\";")
        self.cleaning_progressBar.setProperty("value", 24)
        self.cleaning_progressBar.setObjectName("cleaning_progressBar")
        self.verticalLayout.addWidget(self.cleaning_progressBar)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.cleaning_pushButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cleaning_pushButton.sizePolicy().hasHeightForWidth())
        self.cleaning_pushButton.setSizePolicy(sizePolicy)
        self.cleaning_pushButton.setStyleSheet("font: 8pt \"8514oem\";")
        self.cleaning_pushButton.setObjectName("cleaning_pushButton")
        self.verticalLayout.addWidget(self.cleaning_pushButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "cleaning"))
        self.cleaning_pushButton.setText(_translate("Dialog", "Start Cleaning"))

class a_cleaning_dialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(a_cleaning_dialog, self).__init__(parent)
        self.ui = Ui_CleaningDialog()
        self.ui.setupUi(self)

        self.ui.cleaning_pushButton.clicked.connect(self.start_cleaning)


    def start_cleaning(self):
        def delete_virus_files():

            conn = sqlite3.connect('virus_records.db')
            cursor = conn.cursor()
            
            cursor.execute("SELECT file_path FROM virus_files")
            virus_files = cursor.fetchall()

            if not virus_files:
                QtWidgets.QMessageBox.information(self, "cleaning", "no virus files found in the database.")
                return
            total_files = len(virus_files)
            self.ui.cleaning_progressBar.setMaximum(total_files)
            
            for i, file_path_tuple in enumerate(virus_files, start=1):
                file_path = file_path_tuple[0]
                try:
                    if os.path.exists(file_path):
                        os.remove(file_path)
                        print(f"deleted file: {file_path}")
                    else:
                        print(f"file not found: {file_path}")
                except Exception as e:
                    print(f"error deleting file {file_path}: {e}")

                self.ui.cleaning_progressBar.setValue(i)
                QtCore.QCoreApplication.processEvents()

            # veritabanini temizle
            cursor.execute("DELETE FROM virus_files")
            conn.commit()
            conn.close()
            #print("virus files records cleared from the database.")
            QtWidgets.QMessageBox.information(self, "cleaning", "virus files have been deleted\nand\nrecords cleared from the database.")

        delete_virus_files()