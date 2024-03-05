def ganti_kalimat():
    kalimat = input("Masukkan Satu Kalimat : ")
    cari = input("Masukkan kalimat yang di ganti :")
    ganti = input("Masukkan kalimat baru : ")
    kalimat=kalimat.split(" ")
    for i in range(len(kalimat)) :
        if kalimat[i]==cari:
            kalimat[i]= ganti
    print(" " .join(kalimat))
    
ganti_kalimat()
