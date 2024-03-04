print("Program Menghitung Pendapatan Budi Selama Liburan Musim Panas")
print("="*100)
#input
salary=int(input("Masukkan gaji per jam Budi : "))
work_hours=float(input("Masukkan jam kerja Budi dalam seminggu : "))

#Function Pendapatan Setelah kena Pajak
def taxSalary(x):
    final= x-(x*0.14)
    return final

#Function Pendapatan Sebelum kena Pajak
def noTax(x,y,z):
    return x*(y*z)

#Waktu yang diperlukan
num_Weeks=5

#Pendapatan BELUM KENA PAJAK
gross= noTax(salary,work_hours,num_Weeks)

#Pendapatan KENA PAJAK
netIncome= taxSalary(gross)

#Pengeluaran Pendapatan
Accesories= netIncome*0.1 #Pengeluaran untuk baju dan aksesoris
stationery= netIncome*0.01 #Pengeluaran untuk alat tulis

#Sisa pendapatan pertama
ResidualSalary= netIncome-(Accesories+stationery)

Charity = ResidualSalary*0.25 #Pengeluaran untuk sedekah
setiap_seribu = ResidualSalary*0.25

while setiap_seribu % 1000 ==0 and setiap_seribu > 1000 or setiap_seribu%1000 != 0 and setiap_seribu >1000:
  setiap_seribu -= 1000

uang_sedekah_ril = Charity - setiap_seribu

uang_anak_yatim = (0.30 * uang_sedekah_ril)
uang_dhuafa = (0.70 * uang_sedekah_ril)

#Print
print("Pendapatan Budi selama 5 mingg dengan :\nGaji Rp.%d dan Total Jam Kerja dalam  Seminggu %d Jam " %(salary,work_hours))
print("1. BELUM KENA PAJAK : Rp.%.2f" %gross)
print("2. KENA PAJAK : Rp.%.2f" %netIncome)
print("Pengeluaran Budi :")
print("1. Baju dan Aksesoris : Rp.%.2f" %Accesories)
print("2. Alat Tulis : Rp.%.2f" %stationery)
print("3. Sedekah : RP.%.2f" %uang_sedekah_ril)
print("\t3a. Sedekah untuk Yatim : Rp.%.2f" %uang_anak_yatim)
print("\t3b. Sedekah untuk Dhuafa : Rp.%.2f" %uang_dhuafa)

