from selenium import webdriver #type: ignore
from selenium.webdriver.chrome.service import Service #type: ignore
from selenium.webdriver.support.ui import WebDriverWait #type: ignore
from selenium.webdriver.support import expected_conditions as EC #type: ignore
from selenium.webdriver.common.by import By #type: ignore

import sqlite3
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
    
    print("yeni virus hashleri veritabanina eklendi!")

except Exception as e:
    print(f"Bir hata olustu: {e}")

finally:
    driver.quit()

#-------------------------- txt dosyasindaki hashleri de bu database'e aktardik --------------------------#
