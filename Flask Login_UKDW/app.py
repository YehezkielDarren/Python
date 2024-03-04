from flask import Flask,redirect,url_for,request
import sqlite3


app=Flask(__name__)
#app route
@app.route("/loginAkun", methods=['POST'])
def login_akun():
    if request.method =='POST':
        nama = request.form['nama']
        sandi = request.form['sandi']
        if loginAkun(nama,sandi):
            return redirect(url_for('berhasil', jeneng= nama))
        else:
            return redirect(url_for('err'))
    else:
        return {'Status' : 'ERORR'}
        
@app.route("/daftarAkun", methods=['POST'])
def daftar_akun():
    if request.method=='POST':
        nama = request.form['nama']
        sandi = request.form['sandi']
        if daftarAkun(nama, sandi):
            return redirect(url_for('suksesReg', jeneng=nama))
        else:
            return {'Status' : 'Nama Telah Terdaftar'}
    else:
        return {'Status':'ERROR'}
    
    
@app.route("/hapusAkun", methods=['POST'])
def hapus_akun():
    if request.method=='POST':
        nama = request.form['nama']
        sandi = request.form['sandi']
        if hapusAkun(nama,sandi):
            return redirect(url_for('suksesDel', jeneng=nama))
        else:
            return{'Status' : 'Nama Telah dihapus dari Database'}
    else:
        return {'Status':'ERROR'}
    
#login Error
@app.route("/login/error")
def err():
    return { 'status': 'Login Failed! Please check your username & password!' }
    
#Sukses
@app.route("/login/Success/<nama>", methods=['GET'])
def berhasil(jeneng):
    return{'Status': 'Selamat Datang Kembali %s!'%jeneng}
@app.route("/daftar/Success/<nama>", methods=['GET'])
def sukserReg(jeneng):
    return{'Status': 'Selamat Datang Pengguna Baru : %s!'%jeneng}
@app.route("/hapus/Success/<nama>", methods=['GET'])
def suksesDel(jeneng):
    return{'Status': 'Akun %s Berhasil Terhapus!'%jeneng}
    

#Function DATABEASE Daftar Akun
def daftarAkun(nama, sandi):
    connection=sqlite3.connect("user.db")
    cursor=connection.cursor()
    
    cursor.execute("SELECT 1 FROM user WHERE username=?;", (nama,))
    user_terdaftar=cursor.fetchone()
    
    #Conditional User Terdaftar
    
    if user_terdaftar:
        #Conditional benar => Koneksi ditutup
        connection.close()
        return False #mengembalikan False karena user exist
    cursor.execute("INSERT INTO user (nama,sandi) VALUES(?,?);", (nama,sandi))
    connection.commit()
    connection.close()
    return True
#Function Hapus Akun
def hapusAkun(nama):
    connection=sqlite3.connect("user.db")
    cursor=connection.cursor()
    cursor.execute("SELECT 1 FROM user WHERE nama =?;", (nama,))
    
    #Conditional Benar (akun terdaftar)
    if cursor.fetchone():
        cursor.execute("DELETE FROM user WHERE nama=?;", (nama,))
        connection.commit()
        connection.close()
        return True
    #Conditional salah (akun tidak terdaftar)
    connection.close()
    return False
#Function Masuk Akun
def loginAkun(nama, sandi):
    connection=sqlite3.connect("user.db")
    cursor=connection.cursor()
    #query execute
    cursor.execute("SELECT nama,sandi FROM user WHERE nama=? AND sandi=?;", (nama,sandi))
    count=cursor.fetchone()
    connection.close()
    return count

if __name__ == '__main__':
    app.run(debug=True)
    