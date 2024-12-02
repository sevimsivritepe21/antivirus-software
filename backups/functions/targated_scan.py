import sqlite3
import hashlib
import os
import sys

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

## ilgili alana girilecek path
directory_path = r'C:\Users\sevim\Desktop\rapor'
create_table()

for root, dirs, files in os.walk(directory_path):
    for file in files:
        file_path = os.path.join(root, file)
        file_hash = hash_file(file_path)
        insert_hash(file_path, file_hash)
        print("file:\n", file_path, "\nhash value:\n", file_hash)

print(f"{directory_path} hashes of files in file path added to database.")


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

#birinci kontrol
if common_datas:
    print("virus detected!\ndetected virus hashes:", [hv[1] for hv in common_datas])
else:
    print("the scan is clean.")


#--- dosyanin silinmesi
#for file_path, hash_value in common_datas:
#   if os.path.exists(file_path):
#        os.remove(file_path)
#        print(f"{file_path} has been deleted!!")
#conn1.commit()

conn1.close()
conn2.close()

