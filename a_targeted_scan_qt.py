import sqlite3
import hashlib
import os
import sys


from PyQt5 import QtCore, QtGui, QtWidgets # type: ignore


class Ui_TargetedScanDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(555, 661)

        #pencereye icon ekleyelim
        Dialog.setWindowIcon(QtGui.QIcon("C:/Users/sevim/Desktop/antivirus/qt/icons/target.png")) 

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

#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    dialog = a_targeted_scan_dialog()
#    dialog.show()
#    sys.exit(app.exec_())



