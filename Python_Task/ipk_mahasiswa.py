def IPS(jumlah_matkul,sem):
    tampung_nilai=0
    tot_sks=0
    print(f"Semester {sem+1} : ")
    for mtkul in range(1,jumlah_matkul+1):
        nilai_angka=input("masukkan nilai bobot : ").lower()
        sks=int(input(f"total sks pada matkul ke-{mtkul} : "))
        temp=konversi_nilaiBobot(nilai_angka)
        tampung_nilai+=temp*sks
        tot_sks+=sks
    return round(tampung_nilai/tot_sks,2)

def konversi_nilaiBobot(str):
    if str=='a':
        return 4.0
    elif str=='a-':
        return 3.7
    elif str=='b+':
        return 3.3
    elif str=='b':
        return 3.0
    elif str=='b-':
        return 2.7
    elif str=='c+':
        return 2.3
    elif str=='c':
        return 2.0
    elif str=='d':
        return 1.0
    else:
        return 0

nama=input("Masukkan nama anda : ")
semester=int(input("Total semester yang telah anda tempuh : "))
indPresKum=0
for sem in range(semester):
    jum_mtkl=int(input(f"Masukkan jumlah matkul di semester {sem+1} : "))
    indPresSemester=IPS(jum_mtkl,sem)
    print(f"Total nilai pada semester {sem+1} : {indPresSemester}")
    indPresKum+=indPresSemester
print(f"Hai {nama}, IPK anda selama {semester} semester adalah {indPresKum/semester}")
    
