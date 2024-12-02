#'c:\\'
import hashlib
import os
import sqlite3
import sys

sys.stdout.reconfigure(encoding='utf-8')
#erisim izini olmayan dosyalarin atlanmasi
def hash_file(file_path):
    hasher = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while True:
                chunk = f.read(4096)
                if not chunk:
                    break
                hasher.update(chunk)
    except (OSError, IOError) as e:
        print(f"dosya okumada hata {file_path}: {e}")
        return None
    return hasher.hexdigest()

def create_table():
    conn = sqlite3.connect('c_hashes.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS hashes
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       file_path TEXT,
                       hash_value TEXT)''')
    conn.commit()
    conn.close()

def insert_hashes(hash_data):
    conn = sqlite3.connect('c_hashes.db')
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO hashes (file_path, hash_value) VALUES (?, ?)', hash_data)
    conn.commit()
    conn.close()

directory_path = r'c:\\'

#dosyalari teker teker indiriyor, vakit kaybina sebebiyet veriyor.
#o yüzden taramaya dahil etmiyoruz.
exclude_path = r'C:\Users\sevim\OneDrive'

create_table()

file_hashes = []
for root, dirs, files in os.walk(directory_path):
    #dahil edilmediginin kontrolu
    if exclude_path in root:
        continue
    for file in files:
        file_path = os.path.join(root, file)
        file_hash = hash_file(file_path)
        if file_hash:
            file_hashes.append((file_path, file_hash))
            print(f"Dosya:\n{file_path}\nHash değeri:\n{file_hash}\n")
        else:
            print(f"----! hata olusturdugu icin bu dosya atlaniyor: {file_path}.\n")

if file_hashes:
    insert_hashes(file_hashes)
    print("c bellekteki dosya hashleri veritabanina eklendi.")
else:
    print("hatali kod, veri aktarimi yapilamadi.")
