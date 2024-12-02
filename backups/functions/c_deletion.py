import sqlite3
import os

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

#ortak verilerin, yani viruslerin bulunmasi
common_datas = set((file_path, hash_value) for file_path, hash_value in dosya_bil if (hash_value,) in set2)

#birinci kontrol
if common_datas:
    print("Virus yakalandi!\nYakalanan virusun hashleri:", [hv[1] for hv in common_datas])
else:
    print("Tarama temiz.")


for file_path, hash_value in common_datas:
    #dosyanin silinmesi
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"{file_path} isimli dosya silinmistir!!")
conn1.commit()

conn1.close()
conn2.close()