from selenium import webdriver #type: ignore
from selenium.webdriver.chrome.service import Service #type: ignore
from selenium.webdriver.support.ui import WebDriverWait #type: ignore
from selenium.webdriver.support import expected_conditions as EC #type: ignore
from selenium.webdriver.common.by import By #type: ignore

import sqlite3
import hashlib
import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets # type: ignore
from a_complete_scan_qt import Ui_CompleteScanDialog
from a_cleaning_qt import Ui_CleaningDialog
from a_targeted_scan_qt import Ui_TargetedScanDialog
from a_update_database_qt import Ui_DatabaseDialog



#   direkt ekle
class Ui_CleaningDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(551, 568)

        #pencereye icon ekleyelim
        Dialog.setWindowIcon(QtGui.QIcon("icons/clean.png")) 

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
"{    background-image: url(icons/1.webp);\n"
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



#   direkt ekle
class Ui_TargetedScanDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(555, 661)

        #pencereye icon ekleyelim
        Dialog.setWindowIcon(QtGui.QIcon("icons/target.png")) 

        #flags
        Dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        
        Dialog.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(40, 50, 40, 50)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.other_scan_result_plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.other_scan_result_plainTextEdit.setObjectName("other_scan_result_plainTextEdit")
        self.gridLayout.addWidget(self.other_scan_result_plainTextEdit, 5, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setStyleSheet("font: 63 8.5pt \"Yu Gothic UI Semibold\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 6, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("font: 63 8.5pt \"Yu Gothic UI Semibold\";")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.to_scan_filePath_lineEdit = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.to_scan_filePath_lineEdit.sizePolicy().hasHeightForWidth())
        self.to_scan_filePath_lineEdit.setSizePolicy(sizePolicy)
        self.to_scan_filePath_lineEdit.setObjectName("to_scan_filePath_lineEdit")
        self.verticalLayout.addWidget(self.to_scan_filePath_lineEdit)
        self.scan_path_pushButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scan_path_pushButton.sizePolicy().hasHeightForWidth())
        self.scan_path_pushButton.setSizePolicy(sizePolicy)
        self.scan_path_pushButton.setStyleSheet("font: 63 8.5pt \"Yu Gothic UI Semibold\";")
        self.scan_path_pushButton.setObjectName("scan_path_pushButton")
        self.verticalLayout.addWidget(self.scan_path_pushButton)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setStyleSheet("font: 63 8.5pt \"Yu Gothic UI Semibold\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.targated_scan_results_plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.targated_scan_results_plainTextEdit.setObjectName("targated_scan_results_plainTextEdit")
        self.verticalLayout.addWidget(self.targated_scan_results_plainTextEdit)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(30, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setStyleSheet("font: 63 8.5pt \"Yu Gothic UI Semibold\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(4, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scan_desktop_pushButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scan_desktop_pushButton.sizePolicy().hasHeightForWidth())
        self.scan_desktop_pushButton.setSizePolicy(sizePolicy)
        self.scan_desktop_pushButton.setStyleSheet("font: 63 8.5pt \"Yu Gothic UI Semibold\";")
        self.scan_desktop_pushButton.setObjectName("scan_desktop_pushButton")
        self.horizontalLayout.addWidget(self.scan_desktop_pushButton)
        spacerItem4 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.scan_downloads_pushButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scan_downloads_pushButton.sizePolicy().hasHeightForWidth())
        self.scan_downloads_pushButton.setSizePolicy(sizePolicy)
        self.scan_downloads_pushButton.setStyleSheet("font: 63 8.5pt \"Yu Gothic UI Semibold\";")
        self.scan_downloads_pushButton.setObjectName("scan_downloads_pushButton")
        self.horizontalLayout.addWidget(self.scan_downloads_pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setStyleSheet("font: 8pt \"8514oem\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "targetedScan"))
        self.label_5.setText(_translate("Dialog", "scan results:"))
        self.label.setText(_translate("Dialog", "enter the file path of the file you want to scan:"))
        self.scan_path_pushButton.setText(_translate("Dialog", "scan"))
        self.label_4.setText(_translate("Dialog", "scan results:"))
        self.label_3.setText(_translate("Dialog", "desktop and downloads scan is available if you prefer."))
        self.scan_desktop_pushButton.setText(_translate("Dialog", "desktop"))
        self.scan_downloads_pushButton.setText(_translate("Dialog", "downloands"))
        self.label_2.setText(_translate("Dialog", "TARGATED SCAN"))

class a_targeted_scan_dialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(a_targeted_scan_dialog, self).__init__(parent)
        self.ui = Ui_TargetedScanDialog()
        self.ui.setupUi(self)

        #   buttonlar
        self.ui.scan_path_pushButton.clicked.connect(self.start_targeted_scan)
        self.ui.scan_desktop_pushButton.clicked.connect(self.start_desktop_scan)
        self.ui.scan_downloads_pushButton.clicked.connect(self.start_downloads_scan)

    def start_targeted_scan(self):

        sys.stdout.reconfigure(encoding='utf-8')

        def hash_file(file_path):
            hasher = hashlib.sha256()
            with open(file_path, 'rb') as f:
                while True:
                    chunk = f.read(4096)
                    if not chunk:
                        break
                    hasher.update(chunk)
            return hasher.hexdigest()

        def hash_files_in_directory(directory):
            file_hashes = {}
            for root, dirs, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    file_hash = hash_file(file_path)
                    file_hashes[file_path] = file_hash
            return file_hashes

        def create_table():
            conn = sqlite3.connect('targeted_hashes.db')
            cursor = conn.cursor()
            # tekrar tekrar eklememek icin once varsa sil yoksa direkt olustur tabloyu
            cursor.execute('DROP TABLE IF EXISTS hashes')
            cursor.execute('''CREATE TABLE IF NOT EXISTS hashes
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            file_path TEXT,
                            hash_value TEXT)''')
            conn.commit()
            conn.close()

        def insert_hash(file_path, file_hash):
            conn = sqlite3.connect('targeted_hashes.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO hashes (file_path, hash_value) VALUES (?, ?)', (file_path, file_hash))
            conn.commit()
            conn.close()

        def create_virus_records_table():
            conn = sqlite3.connect('virus_records.db')
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS virus_files
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            file_path TEXT,
                            hash_value TEXT)''')
            conn.commit()
            conn.close()

        def insert_virus_record(file_path, file_hash):
            conn = sqlite3.connect('virus_records.db')
            cursor = conn.cursor()
            # girdiler ciftlenmesin
            cursor.execute('SELECT * FROM virus_files WHERE file_path = ? AND hash_value = ?', (file_path, file_hash))
            if cursor.fetchone() is None:
                cursor.execute('INSERT INTO virus_files (file_path, hash_value) VALUES (?, ?)', (file_path, file_hash))
                conn.commit()
            conn.close()

        directory_path = self.ui.to_scan_filePath_lineEdit.text()
        if not directory_path or not os.path.isdir(directory_path):
            self.ui.targated_scan_results_plainTextEdit.setPlainText("invalid directory path.")
            return
        
        create_table()
        create_virus_records_table()

        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_hash = hash_file(file_path)
                insert_hash(file_path, file_hash)

        #print(f"{directory_path} hashes of files in file path added to database.")

        conn1 = sqlite3.connect("targeted_hashes.db")
        c1 = conn1.cursor()
        conn2 = sqlite3.connect("updated_virus_hashes.db")
        c2 = conn2.cursor()

        c1.execute("SELECT file_path, hash_value FROM hashes")
        dosya_bil = c1.fetchall()
        c2.execute("SELECT current_virus_hash FROM sha256_hashes")
        virus_bil = c2.fetchall()

        set1 = set(dosya_bil)
        set2 = set(virus_bil)

        # ortak verilerin, yani viruslerin bulunmasi
        common_datas = set((file_path, hash_value) for file_path, hash_value in dosya_bil if (hash_value,) in set2)

        QtWidgets.QMessageBox.information(self, "successful!", "targeted scan is completed!\nprinting the results...")

        if common_datas:
            self.ui.targated_scan_results_plainTextEdit.appendPlainText("virus detected!\ndetected virus hashes:\n")
            for file_path, hash_value in common_datas:
                self.ui.targated_scan_results_plainTextEdit.appendPlainText(f"->file: {file_path}\n->hash value: {hash_value}\n")
                insert_virus_record(file_path, hash_value)
        else:
            self.ui.targated_scan_results_plainTextEdit.appendPlainText("scan is clean.")



    def start_desktop_scan(self):
        sys.stdout.reconfigure(encoding='utf-8')

        def hash_file(file_path):
            hasher = hashlib.sha256()
            with open(file_path, 'rb') as f:
                while True:
                    chunk = f.read(4096)
                    if not chunk:
                        break
                    hasher.update(chunk)
            return hasher.hexdigest()

        def hash_files_in_directory(directory):
            file_hashes = {}
            for root, dirs, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    file_hash = hash_file(file_path)
                    file_hashes[file_path] = file_hash
            return file_hashes

        def create_table():
            conn = sqlite3.connect('desktop_hashes.db')
            cursor = conn.cursor()

            cursor.execute('DROP TABLE IF EXISTS hashes')
            cursor.execute('''CREATE TABLE IF NOT EXISTS hashes
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            file_path TEXT,
                            hash_value TEXT)''')
            conn.commit()
            conn.close()

        def insert_hash(file_path, file_hash):
            conn = sqlite3.connect('desktop_hashes.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO hashes (file_path, hash_value) VALUES (?, ?)', (file_path, file_hash))
            conn.commit()
            conn.close()

        def create_virus_records_table():
            conn = sqlite3.connect('virus_records.db')
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS virus_files
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            file_path TEXT,
                            hash_value TEXT)''')
            conn.commit()
            conn.close()

        def insert_virus_record(file_path, file_hash):
            conn = sqlite3.connect('virus_records.db')
            cursor = conn.cursor()
            # girdiler ciftlenmesin
            cursor.execute('SELECT * FROM virus_files WHERE file_path = ? AND hash_value = ?', (file_path, file_hash))
            if cursor.fetchone() is None:
                cursor.execute('INSERT INTO virus_files (file_path, hash_value) VALUES (?, ?)', (file_path, file_hash))
                conn.commit()
            conn.close()

        directory_path = r'C:\Users\sevim\Desktop'

        create_table()
        create_virus_records_table()

        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_hash = hash_file(file_path)
                insert_hash(file_path, file_hash)

        #print(f"{directory_path} hashes of files in file path added to database.")

        conn1 = sqlite3.connect("desktop_hashes.db")
        c1 = conn1.cursor()
        conn2 = sqlite3.connect("updated_virus_hashes.db")
        c2 = conn2.cursor()

        c1.execute("SELECT file_path, hash_value FROM hashes")
        dosya_bil = c1.fetchall()
        c2.execute("SELECT current_virus_hash FROM sha256_hashes")
        virus_bil = c2.fetchall()

        set1 = set(dosya_bil)
        set2 = set(virus_bil)

        common_datas2 = set((file_path, hash_value) for file_path, hash_value in dosya_bil if (hash_value,) in set2)

        QtWidgets.QMessageBox.information(self, "successful!", "desktop scan is completed!\nprinting the results...")


        if common_datas2:
            self.ui.other_scan_result_plainTextEdit.appendPlainText("-*-desktop scan-*-\n")
            self.ui.other_scan_result_plainTextEdit.appendPlainText("virus detected!\ndetected virus hashes:\n")
            for file_path, hash_value in common_datas2:
                self.ui.other_scan_result_plainTextEdit.appendPlainText(f"->file: {file_path}\n->hash value: {hash_value}\n")
                insert_virus_record(file_path, hash_value)
        else:
            self.ui.other_scan_result_plainTextEdit.appendPlainText("scan is clean.")
        

    def start_downloads_scan(self):
        sys.stdout.reconfigure(encoding='utf-8')

        def hash_file(file_path):
            hasher = hashlib.sha256()
            with open(file_path, 'rb') as f:
                while True:
                    chunk = f.read(4096)
                    if not chunk:
                        break
                    hasher.update(chunk)
            return hasher.hexdigest()

        def hash_files_in_directory(directory):
            file_hashes = {}
            for root, dirs, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    file_hash = hash_file(file_path)
                    file_hashes[file_path] = file_hash
            return file_hashes

        def create_table():
            conn = sqlite3.connect('downloads_hashes.db')
            cursor = conn.cursor()

            cursor.execute('DROP TABLE IF EXISTS hashes')
            cursor.execute('''CREATE TABLE IF NOT EXISTS hashes
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            file_path TEXT,
                            hash_value TEXT)''')
            conn.commit()
            conn.close()

        def insert_hash(file_path, file_hash):
            conn = sqlite3.connect('downloads_hashes.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO hashes (file_path, hash_value) VALUES (?, ?)', (file_path, file_hash))
            conn.commit()
            conn.close()

        def create_virus_records_table():
            conn = sqlite3.connect('virus_records.db')
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS virus_files
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            file_path TEXT,
                            hash_value TEXT)''')
            conn.commit()
            conn.close()

        def insert_virus_record(file_path, file_hash):
            conn = sqlite3.connect('virus_records.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM virus_files WHERE file_path = ? AND hash_value = ?', (file_path, file_hash))
            if cursor.fetchone() is None:
                cursor.execute('INSERT INTO virus_files (file_path, hash_value) VALUES (?, ?)', (file_path, file_hash))
                conn.commit()
            conn.close()

        directory_path = r'C:\Users\sevim\Downloads'

        create_table()
        create_virus_records_table()

        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_hash = hash_file(file_path)
                insert_hash(file_path, file_hash)

        #print(f"{directory_path} hashes of files in file path added to database.")

        conn1 = sqlite3.connect("downloads_hashes.db")
        c1 = conn1.cursor()
        conn2 = sqlite3.connect("updated_virus_hashes.db")
        c2 = conn2.cursor()

        c1.execute("SELECT file_path, hash_value FROM hashes")
        dosya_bil = c1.fetchall()
        c2.execute("SELECT current_virus_hash FROM sha256_hashes")
        virus_bil = c2.fetchall()

        set1 = set(dosya_bil)
        set2 = set(virus_bil)

        common_datas3 = set((file_path, hash_value) for file_path, hash_value in dosya_bil if (hash_value,) in set2)

        QtWidgets.QMessageBox.information(self, "successful!", "downloads scan is completed!\nprinting the results...")


        if common_datas3:
            self.ui.other_scan_result_plainTextEdit.appendPlainText("-*-downloads scan-*-\n")
            self.ui.other_scan_result_plainTextEdit.appendPlainText("virus detected!\ndetected virus hashes:\n")
            for file_path, hash_value in common_datas3:
                self.ui.other_scan_result_plainTextEdit.appendPlainText(f"->file: {file_path}\n->hash value: {hash_value}\n")
                insert_virus_record(file_path, hash_value)
        else:
            self.ui.other_scan_result_plainTextEdit.appendPlainText("scan is clean.")

        #print(f"{directory_path} hashes of files in file path added to database.")

        conn1 = sqlite3.connect("desktop_hashes.db")
        c1 = conn1.cursor()
        conn2 = sqlite3.connect("updated_virus_hashes.db")
        c2 = conn2.cursor()

        c1.execute("SELECT file_path, hash_value FROM hashes")
        dosya_bil = c1.fetchall()
        c2.execute("SELECT current_virus_hash FROM sha256_hashes")
        virus_bil = c2.fetchall()

        set1 = set(dosya_bil)
        set2 = set(virus_bil)

        common_datas2 = set((file_path, hash_value) for file_path, hash_value in dosya_bil if (hash_value,) in set2)

        QtWidgets.QMessageBox.information(self, "successful!", "desktop scan is completed!\nprinting the results...")


        if common_datas2:
            self.ui.other_scan_result_plainTextEdit.appendPlainText("-*-desktop scan-*-\n")
            self.ui.other_scan_result_plainTextEdit.appendPlainText("virus detected!\ndetected virus hashes:\n")
            for file_path, hash_value in common_datas2:
                self.ui.other_scan_result_plainTextEdit.appendPlainText(f"->file: {file_path}\n->hash value: {hash_value}\n")
        else:
            self.ui.other_scan_result_plainTextEdit.appendPlainText("scan is clean.")
        

    def start_downloads_scan(self):
        sys.stdout.reconfigure(encoding='utf-8')

        def hash_file(file_path):
            hasher = hashlib.sha256()
            with open(file_path, 'rb') as f:
                while True:
                    chunk = f.read(4096)
                    if not chunk:
                        break
                    hasher.update(chunk)
            return hasher.hexdigest()

        def hash_files_in_directory(directory):
            file_hashes = {}
            for root, dirs, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    file_hash = hash_file(file_path)
                    file_hashes[file_path] = file_hash
            return file_hashes

        def create_table():
            conn = sqlite3.connect('downloads_hashes.db')
            cursor = conn.cursor()

            cursor.execute('DROP TABLE IF EXISTS hashes')
            cursor.execute('''CREATE TABLE IF NOT EXISTS hashes
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            file_path TEXT,
                            hash_value TEXT)''')
            conn.commit()
            conn.close()

        def insert_hash(file_path, file_hash):
            conn = sqlite3.connect('downloads_hashes.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO hashes (file_path, hash_value) VALUES (?, ?)', (file_path, file_hash))
            conn.commit()
            conn.close()

        directory_path = r'C:\Users\sevim\Downloads'
        create_table()

        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_hash = hash_file(file_path)
                insert_hash(file_path, file_hash)

        #print(f"{directory_path} hashes of files in file path added to database.")

        conn1 = sqlite3.connect("downloads_hashes.db")
        c1 = conn1.cursor()
        conn2 = sqlite3.connect("updated_virus_hashes.db")
        c2 = conn2.cursor()

        c1.execute("SELECT file_path, hash_value FROM hashes")
        dosya_bil = c1.fetchall()
        c2.execute("SELECT current_virus_hash FROM sha256_hashes")
        virus_bil = c2.fetchall()

        set1 = set(dosya_bil)
        set2 = set(virus_bil)

        common_datas3 = set((file_path, hash_value) for file_path, hash_value in dosya_bil if (hash_value,) in set2)

        QtWidgets.QMessageBox.information(self, "successful!", "downloads scan is completed!\nprinting the results...")


        if common_datas3:
            self.ui.other_scan_result_plainTextEdit.appendPlainText("-*-downloads scan-*-\n")
            self.ui.other_scan_result_plainTextEdit.appendPlainText("virus detected!\ndetected virus hashes:\n")
            for file_path, hash_value in common_datas3:
                self.ui.other_scan_result_plainTextEdit.appendPlainText(f"->file: {file_path}\n->hash value: {hash_value}\n")
        else:
            self.ui.other_scan_result_plainTextEdit.appendPlainText("scan is clean.")



#   direkt ekle
class Ui_CompleteScanDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(469, 438)
        
        Dialog.setWindowIcon(QtGui.QIcon("icons/flag.png"))
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
                self.ui.complete_scan_result_plainTextEdit.appendPlainText("The scan is clean.")

            conn1.close()
            conn2.close()

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "error", f"an error occurred: {e}")



#   direkt ekle
class Ui_DatabaseDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(510, 508)

        #pencereye icon ekleyelim
        Dialog.setWindowIcon(QtGui.QIcon("icons/update.png")) 

        #flags
        Dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)


        Dialog.setStyleSheet("QDialog\n"
"{\n"
"    background-image: url(icons/3.webp);\n"
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
        self.update_dateTimeEdit.setReadOnly(True) 
        self.horizontalLayout.addWidget(self.update_dateTimeEdit)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "updateDatabase"))
        self.update_pushButton.setText(_translate("Dialog", "Update Database"))
        self.label.setText(_translate("Dialog", "warning! a robot test must be passed when accessing the site where updates are received."))
        self.label_2.setText(_translate("Dialog", "please do the test correctly!"))
        self.label_3.setText(_translate("Dialog", "Last Updated:"))

class a_update_dialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(a_update_dialog, self).__init__(parent)
        self.ui = Ui_DatabaseDialog()
        self.ui.setupUi(self)

        #   pushButton
        self.ui.update_pushButton.clicked.connect(self.update_database)

        #   button'a son basilma bilgisini text dosyasinda tutacagiz
        self.date_file_path = 'last_update_date.txt'
        self.load_last_update_date()

    def load_last_update_date(self):
        if os.path.exists(self.date_file_path):
            with open(self.date_file_path, 'r') as file:
                last_update_date_str = file.read().strip()
                #   string'in date'e cevirilmesi
                last_update_date = QtCore.QDateTime.fromString(last_update_date_str, "dd.MM.yyyy HH:mm:ss")
        else:
            #   text bos ise varsayilan tarih
            last_update_date = QtCore.QDateTime.fromString("01.01.2000 00:00:00", "dd.MM.yyyy HH:mm:ss")

        self.ui.update_dateTimeEdit.setDateTime(last_update_date)
        self.ui.update_dateTimeEdit.setDisplayFormat("dd.MM.yyyy HH:mm:ss")
        self.ui.update_dateTimeEdit.show()

    #   text dosyasini guncelle ve kaydet
    def save_last_update_date(self):
        last_update_date_str = self.ui.update_dateTimeEdit.dateTime().toString("dd.MM.yyyy HH:mm:ss")
        with open(self.date_file_path, 'w') as file:
            file.write(last_update_date_str)

    def update_database(self):

        chrome_driver_path = 'd:/chromedriver-win64/chromedriver.exe'
        service = Service(chrome_driver_path)

        driver = webdriver.Chrome(service=service)

        driver.get('https://bazaar.abuse.ch/browse/')

        wait = WebDriverWait(driver, 60) #bekleme süresidir, robot testi var sitede artirmak mantikli

        try:
            hashes = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'table.table tbody tr td:nth-child(2)')))
            #sitedeki tablonun 2. sutunda mevcut olan hash degerlerine bu sekilde erisiyoruz
            new_hash_values = [hash.text.strip() for hash in hashes]

            #guncel virusleri database'e aktar
            #254. satirdan itibaren dinamik bir sekilde eklemeye baslar?
            conn = sqlite3.connect('updated_virus_hashes.db')
            cursor = conn.cursor()

            cursor.execute('''CREATE TABLE IF NOT EXISTS sha256_hashes (
                id INTEGER PRIMARY KEY AUTOINCREMENT, current_virus_hash TEXT NOT NULL)''')

            #daha once veritabanında olan degerleri cek
            cursor.execute("SELECT current_virus_hash FROM sha256_hashes")
            existing_hashes = [row[0] for row in cursor.fetchall()]

            #cakismayanlari bul ve ekle
            unique_new_hashes = list(set(new_hash_values) - set(existing_hashes))
            for hash_value in unique_new_hashes:
                cursor.execute('INSERT INTO sha256_hashes (current_virus_hash) VALUES (?)', (hash_value,))
            #database'in sonuna ekliyor yeni eklenenleri
            
            conn.commit()
            conn.close()

            QtWidgets.QMessageBox.information(self, "successful!", "new virus hashes has been added to virus database!")
            ## print("yeni virus hashleri veritabanina eklendi!")

            #   son guncellenme tarihini goster ve text dosyasina yazdir
            current_time = QtCore.QDateTime.currentDateTime()
            self.ui.update_dateTimeEdit.setDateTime(current_time)
            self.save_last_update_date()


        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "error", f"an error occurred: {e}")
            ## print(f"Bir hata olustu: {e}")

        finally:          
            driver.quit()

        #-------------------------- txt dosyasindaki hashleri de bu database'e aktardik --------------------------#




GREEN_STYLE = """
    QFrame {
        background-color: rgb(65, 176, 110);
        border-radius: 10px;
        }
        """

RED_STYLE = """
    QFrame {
        background-color: rgb(255, 0, 0);
        border-radius: 10px;
        }
         """

LABEL_STYLE1 = """
    QLabel {
        font: 75 16pt "Cooper Black";
        color: black;
        }
        """
        
LABEL_STYLE2 = """
    QLabel {
        font: 75 9pt "Ebrima";
        font-weight: bold;
        color: black;
        }
        """


class Ui_MainWindow(object):
    
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        
        

        #pencereye icon ekleyelim
        MainWindow.setWindowIcon(QtGui.QIcon("icons/virus.png")) 

        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.frame1.setFont(font)
        self.frame1.setStyleSheet(RED_STYLE)

        self.frame1_layout = QtWidgets.QVBoxLayout(self.frame1)
        self.frame1_layout.setAlignment(QtCore.Qt.AlignCenter)
        self.frame1_layout.setContentsMargins(20, 20, 20, 20)
        self.frame1_layout.setSpacing(10)
        #self.label_5 = QtWidgets.QLabel("SECURE!", self.frame1)
        #self.label_5.setStyleSheet(LABEL_STYLE1)
        #self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        #self.frame1_layout.addWidget(self.label_5)

        #self.label_9 = QtWidgets.QLabel("don't forget to scan your computer frequently!!", self.frame1)
        #self.label_9.setStyleSheet(LABEL_STYLE2)
        #self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        #self.frame1_layout.addWidget(self.label_9)

        #self.image_label = QtWidgets.QLabel(self.frame1)
        #pixmap = QtGui.QPixmap("C:/Users/sevim/Desktop/antivirus/qt/icons/flower.png")
        #scaled_pixmap = pixmap.scaled(55, 55, QtCore.Qt.KeepAspectRatio)
        #self.image_label.setPixmap(scaled_pixmap)
        #self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        #self.frame1_layout.addWidget(self.image_label)

        self.image_label = QtWidgets.QLabel(self.frame1)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.frame1_layout.addWidget(self.image_label)


        # -- scan -- #        
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame1)
        self.verticalLayout_6.setContentsMargins(44, 44, 44, 44)
        self.verticalLayout_6.setSpacing(44)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.frame1)
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.label_9 = QtWidgets.QLabel(self.frame1)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.horizontalLayout.addWidget(self.frame1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_3.setSpacing(10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(8)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"    border: 1px solid rgb(21, 21, 21);\n"
"    border-radius: 40px;\n"
#"    border: none;\n"
"    background-image: url(icons/scan.jpg);\n"
"    background-position: center;\n"
"}")
        


        # -- target -- #     
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_3.addWidget(self.pushButton_8, 0, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    border: 1px solid rgb(21, 21, 21);\n"
"    border-radius: 40px;\n"
#"    border: none;\n"
"    background-image: url(icons/target.jpg);\n"
"    background-position: center;\n"
"}")
        


        # -- cleaning -- #     
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_3.addWidget(self.pushButton_6, 0, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    border: 1px solid rgb(21, 21, 21);\n"
"    border-radius: 40px;\n"
#"    border: none;\n"
"    background-image: url(icons/cleaning.jpg);\n"
"    background-position: center;\n"
"}")
        

        # -- database -- #
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_3.addWidget(self.pushButton_5, 2, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    border: 1px solid rgb(21, 21, 21);\n"
"    border-radius: 40px;\n"
#"    border: none;\n"
"    background-image: url(icons/database.jpg);\n"
"    background-position: center;\n"
"}")
        


        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_3.addWidget(self.pushButton_7, 2, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(8)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 3, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(8)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 3, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1090, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #   pushButton signal-slot
        self.pushButton_8.clicked.connect(self.open_complete_scan_dialog)
        self.pushButton_6.clicked.connect(self.open_a_targeted_scan_dialog) 
        self.pushButton_5.clicked.connect(self.open_a_cleaning_dialog)
        self.pushButton_7.clicked.connect(self.open_a_database_dialog)
        

        self.set_frame_style_and_image("red")
        #self.change_style_button = QtWidgets.QPushButton("Change Style", self.centralwidget)
        #self.change_style_button.clicked.connect(self.toggle_frame_style)
        self.pushButton_5.clicked.connect(self.toggle_frame_style)
        
        #self.horizontalLayout.addWidget(self.change_style_button)

        #       self.toggle_frame_style()

    def set_frame_style_and_image(self, style):

        if style == "red":
            self.frame1.setStyleSheet(RED_STYLE)
            self.label_5.setText("UNSECURE!")
            self.label_5.setStyleSheet(LABEL_STYLE1)
            self.label_5.setAlignment(QtCore.Qt.AlignCenter)
            self.frame1_layout.addWidget(self.label_5)

            self.label_9.setText("<your computer is at risk>\nscan your computer!\nclean up the viruses!!")
            self.label_9.setStyleSheet(LABEL_STYLE2)
            self.label_9.setAlignment(QtCore.Qt.AlignCenter)
            self.frame1_layout.addWidget(self.label_9)
            pixmap = QtGui.QPixmap("icons/skull.png")

        elif style == "green":
            self.frame1.setStyleSheet(GREEN_STYLE)
            self.label_5.setText("SECURE!")
            self.label_5.setStyleSheet(LABEL_STYLE1)
            self.label_5.setAlignment(QtCore.Qt.AlignCenter)
            self.frame1_layout.addWidget(self.label_5)

            self.label_9.setText("don't forget to scan your computer frequently!!")
            self.label_9.setStyleSheet(LABEL_STYLE2)
            self.label_9.setAlignment(QtCore.Qt.AlignCenter)
            self.frame1_layout.addWidget(self.label_9)
            pixmap = QtGui.QPixmap("icons/flower.png")

        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)

    def toggle_frame_style(self):
        current_style = self.frame1.styleSheet()
        if RED_STYLE in current_style:
            self.set_frame_style_and_image("green")
        else:
            self.set_frame_style_and_image("red")    


    def check_virus_records(self):
        conn = sqlite3.connect('virus_records.db')
        cursor = conn.cursor()

        cursor.execute("SELECT file_path FROM virus_files")
        virus_files = cursor.fetchall()
        conn.close()

        if not virus_files:
            self.set_frame_style_and_image("green")
        else:
            self.set_frame_style_and_image("red")

    def update_frame_style(self):
        conn = sqlite3.connect('virus_records.db')
        cursor = conn.cursor()

        cursor.execute("SELECT file_path FROM virus_files")
        virus_files = cursor.fetchall()
        conn.close()

        if not virus_files:
            self.frame1.setStyleSheet(GREEN_STYLE)
            self.label_5.setText("SECURE!")
            self.label_5.setStyleSheet(LABEL_STYLE1)
            self.label_5.setAlignment(QtCore.Qt.AlignCenter)
            self.frame1_layout.addWidget(self.label_5)

            self.label_9.setText("don't forget to scan your computer frequently!!")
            self.label_9.setStyleSheet(LABEL_STYLE2)
            self.label_9.setAlignment(QtCore.Qt.AlignCenter)
            self.frame1_layout.addWidget(self.label_9)
            pixmap = QtGui.QPixmap("icons/flower.png")

        else:
            self.frame1.setStyleSheet(RED_STYLE)
            self.label_5.setText("UNSECURE!")
            self.label_5.setStyleSheet(LABEL_STYLE1)
            self.label_5.setAlignment(QtCore.Qt.AlignCenter)
            self.frame1_layout.addWidget(self.label_5)

            self.label_9.setText("<your computer is at risk>\nclean up the viruses!!")
            self.label_9.setStyleSheet(LABEL_STYLE2)
            self.label_9.setAlignment(QtCore.Qt.AlignCenter)
            self.frame1_layout.addWidget(self.label_9)
            pixmap = QtGui.QPixmap("icons/skull.png")

        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Antivirus"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "antivirus"))
        self.label_10.setText(_translate("MainWindow", "Targeted Scan"))
        self.label_6.setText(_translate("MainWindow", "Complete Scan"))
        self.label_11.setText(_translate("MainWindow", "Cleaning"))
        self.label_12.setText(_translate("MainWindow", "Update Database"))

    def open_complete_scan_dialog(self):
        self.complete_scan_dialog = a_complete_scan_dialog()
        self.complete_scan_dialog.exec_()

    def open_a_targeted_scan_dialog(self):
        self.targeted_scan_dialog = a_targeted_scan_dialog()
        self.targeted_scan_dialog.exec_()

    def open_a_cleaning_dialog(self):
        self.cleaning_dialog = a_cleaning_dialog()
        self.cleaning_dialog.exec_()

    def open_a_database_dialog(self):
        self.database_dialog = a_update_dialog()
        self.database_dialog.exec_()

#   for running file
#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    dialog =a_cleaning_dialog()
#    dialog.show()
#    sys.exit(app.exec_())
