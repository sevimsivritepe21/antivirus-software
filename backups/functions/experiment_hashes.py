import hashlib
import os
import sqlite3
import sys

#dosya turkce karakter icerebilir, hatalari bu satirla engelleriz
sys.stdout.reconfigure(encoding='utf-8')

def hash_file(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while True:
            #komutu ile dosya 4096 baytlik chunklara bolunerek okunur
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
    conn = sqlite3.connect('file_hashes.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS hashes
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       file_path TEXT,
                       hash_value TEXT)''')
    conn.commit()
    conn.close()

def insert_hash(file_path, file_hash):
    conn = sqlite3.connect('file_hashes.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO hashes (file_path, hash_value) VALUES (?, ?)', (file_path, file_hash))
    conn.commit()
    conn.close()

directory_path = r'C:\Users\sevim\Desktop\antivirus\experiments'
create_table()

for root, dirs, files in os.walk(directory_path):
    for file in files:
        file_path = os.path.join(root, file)
        file_hash = hash_file(file_path)
        insert_hash(file_path, file_hash)
        print("Dosya:\n", file_path, "\nHash degeri:\n", file_hash)

print("Dosya hashleri veritabanına eklendi.")
    
    
    

