def cek_duplikat(string):
    # buat set kosong
    karakter_set = set()
    # cek semua karakter dalam string satu-persatu
    for karakter in string:
    # apakah karakter ini ada dalam set?
        if karakter in karakter_set:
    # ternyata ada, berarti duplikat
    # hentikan pengecekan, langsung return
            return True
        else:
    # jika belum ada, masukkan dalam set
            karakter_set.add(karakter)
    # setelah looping semua karakter, tidak ada yang sama
    return False
# test case
string1 = 'Alexander the Great' # duplikat
print(cek_duplikat(string1))
string2 = 'UKDW' # semua unik
print(cek_duplikat(string2))