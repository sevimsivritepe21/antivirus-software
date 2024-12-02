import sqlite3

conn2 = sqlite3.connect("virus_hashes.db")
c2 = conn2.cursor()
c2.execute("SELECT virus_info FROM virus_hashleri")
virus_bil = c2.fetchall()
aranan_hash="ffafaad5b690ab40ba34fe7e6ae41eb032cf834a"


#fetchall liste şeklinde deger dondurur
#bu yuzden listedeki elemanlari gezmemiz lazim
virus_bulundu = False
for veri in virus_bil:
    #tuple'in ilk elemanini sorgular
    if veri[0] == aranan_hash:
        virus_bulundu = True
        break

if virus_bulundu:
    print("CATCH")
else:
    print("Tarama temiz.")

conn2.close()


