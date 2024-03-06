"""Menampilkan Tahun Berikutnya dengan Setiap Angka Berbeda"""
def year_4():
    Tahun_Dasar = int(input("Masukkan Tahun Minimum (4 digit) : "))
    while True:
        if Tahun_Dasar>=0:
            while Tahun_Dasar<9:
                Tahun_Dasar+=1
            digitSatu= (Tahun_Dasar//1000)%10
            digitDUa= (Tahun_Dasar//100)%10
            digitTIga=(Tahun_Dasar//10)%10
            digitEmpat=(Tahun_Dasar%10)
        else:
            return "Input MELEBIHI atau KURANG dari ketentuan"
        if digitSatu==digitDUa:
            Tahun_Dasar+=1
        elif digitSatu==digitTIga:
            Tahun_Dasar+=1
        elif digitSatu ==digitEmpat:
            Tahun_Dasar+=1
        elif digitDUa== digitTIga:
            Tahun_Dasar+=1
        elif digitDUa==digitEmpat:
            Tahun_Dasar+=1
        elif digitTIga==digitEmpat:
            Tahun_Dasar+=1
        else:
            print(Tahun_Dasar)
            break
                
year_4()


