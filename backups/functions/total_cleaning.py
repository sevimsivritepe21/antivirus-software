import sqlite3
import os

def delete_virus_files():

    conn = sqlite3.connect('virus_records.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT file_path FROM virus_files")
    virus_files = cursor.fetchall()
    
    if not virus_files:
        print("no virus files found in the database.")
        return

    for file_path_tuple in virus_files:
        file_path = file_path_tuple[0]
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"deleted file: {file_path}")
            else:
                print(f"file not found: {file_path}")
        except Exception as e:
            print(f"error deleting file {file_path}: {e}")

    # veritabanini temizle
    cursor.execute("DELETE FROM virus_files")
    conn.commit()
    conn.close()
    print("virus files records cleared from the database.")

delete_virus_files()