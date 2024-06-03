import re

def validasi_kartu_kredit(nomor_kartu):
    # tulis jawaban anda hanya di dalam fungsi ini saja
    # fungsi ini harus return sebuah string sesuai ketentuan
    tidak_valid=re.findall("\D*",nomor_kartu)[0]
    if len(nomor_kartu)<16 or tidak_valid!="":
        return "Tidak valid"
    else:
        angka_8=re.findall("8{4}",nomor_kartu)
        awal_reguler=re.findall("^6", nomor_kartu)
        awal_platinum=re.findall("^4",nomor_kartu)
        if awal_platinum:
            if angka_8:
                return "Valid Platinum"
            else:
                return "Valid Reguler"
        if awal_reguler:
            return "Valid Reguler"

nomor='42345678888888823456'
hasil=validasi_kartu_kredit(nomor)
print(hasil)