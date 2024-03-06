"""Menampilkan Tahun Berikutnya dengan Setiap Angka Berbeda"""
def year_4():
    Tahun_Dasar = int(input("Masukkan Tahun Minimum (4 digit) : "))
    while True:
        if Tahun_Dasar<10000 and Tahun_Dasar>=0:
            digitSatu= (Tahun_Dasar//1000)%10
            digitDUa= (Tahun_Dasar//100)%10
            digitTIga=(Tahun_Dasar//10)%10
            digitEmpat=(Tahun_Dasar%10)
        else:
            return "Input MELEBIHI atau KURANG dari ketentuan"
        if digitSatu==digitDUa or digitSatu==digitTIga or digitSatu ==digitEmpat or digitDUa== digitTIga or digitDUa==digitEmpat or digitTIga==digitEmpat:
            Tahun_Dasar+=1
        else:
            print(Tahun_Dasar)
            break
                
year_4()
        