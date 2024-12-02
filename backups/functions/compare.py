import sqlite3

conn1 = sqlite3.connect("file_hashes.db")
c1 = conn1.cursor()
conn2 = sqlite3.connect("updated_virus_hashes.db")
c2 = conn2.cursor()

c1.execute("SELECT hash_value FROM hashes")
dosya_bil = c1.fetchall()
c2.execute("SELECT current_virus_hash FROM sha256_hashes")
virus_bil = c2.fetchall()
#fetchall liste şeklinde deger dondurur

#verileri set olarak saklayarak kiyaslama yapmak
#isimizi kolaylastiracaktir
set1=set(dosya_bil)
set2=set(virus_bil)

#iki veritabanında da bulunan verileri bulmaliyiz
ortak_veriler = set1 & set2
virus_bulundu = False
for h_dosya in set1:
    if h_dosya in set2:
        virus_bulundu = True
        break

if virus_bulundu:
    print("Virus yakalandi!\nYakalanan virusun hashi:", ortak_veriler)
else:
    print("Tarama temiz.")
