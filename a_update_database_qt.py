from PyQt5 import QtCore, QtGui, QtWidgets # type: ignore

from selenium import webdriver #type: ignore
from selenium.webdriver.chrome.service import Service #type: ignore
from selenium.webdriver.support.ui import WebDriverWait #type: ignore
from selenium.webdriver.support import expected_conditions as EC #type: ignore
from selenium.webdriver.common.by import By #type: ignore
import os

import sqlite3


class Ui_DatabaseDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(510, 508)

        #pencereye icon ekleyelim
        Dialog.setWindowIcon(QtGui.QIcon("C:/Users/sevim/Desktop/antivirus/qt/icons/update.png")) 

        #flags
        Dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)


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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = a_update_dialog()
    dialog.show()
    sys.exit(app.exec_())

