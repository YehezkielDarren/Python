import sqlite3

def createTable():
    connection = sqlite3.connect("mahasiswa.db")
    cursor=connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mahasiswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            nim TEXT NOT NULL,
            jurusan TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()
    
#menambahkan mahasiswa baru
def  tambahMahasiswa(nama,nim,jurusan):
    connection=sqlite3.connect("mahasiswa.db")
    cursor=connection.cursor()
    cursor.execute("INSERT INTO mahasiswa(nama,nim,jurusan) VALUES(?,?,?);", (nama,nim,jurusan))
    
    connection.commit()
    connection.close()

#menambahkan mahasiswa
def tampilMahasiswa():
    connection=sqlite3.connect("mahasiswa.db")
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM mahasiswa;")
    
    for row in cursor.fetchall():
        print(row)
    connection.commit()
    connection.close()
    
#mengupdate data mahasiswa
def updateMahasiswa(nim, newNama, newJurusan):
    connection=sqlite3.connect("mahasiswa.db")
    cursor=connection.cursor()
    cursor.execute("UPDATE mahasiswa SET(nama, jurusan)=(?,?) WHERE nim =?;", (newNama,newJurusan,nim))
    connection.commit()
    connection.close()
    
#menghapus data Mahasiswa berdasarkan nim
def hapusMahasiswa(nim):
    connection=sqlite3.connect("mahasiswa.db")
    cursor=connection.cursor()
    cursor.execute("DELETE FROM mahasiswa WHERE nim=?;",(nim,))
    connection.commit()
    connection.close()
    
#Tampilan SEMUA

createTable()

tambahMahasiswa("Darren","71231023","Informatika")
tambahMahasiswa("Bonar Manalu", "22334455", "Teknik Komedi")
tambahMahasiswa("Candra Mukti Wicaksono", "33445566", "Sistem Komedi Tunggal")

print("Daftar Mahasiwa : ")
tampilMahasiswa()

updateMahasiswa("71231023","Yehezkiel Darren","Manajemen Perbankan")
print("\nData Mahasiwa Terbaru : ")
tampilMahasiswa()


hapusMahasiswa("71231023")
print("\nData Mahasiwa Terbaru : ")
tampilMahasiswa()
