def Kabisat(tahun):
    if tahun % 4 == 0 :
        if tahun%100==0 :
            if tahun%400==0 :
                print("%s merupakan Tahun Kabisat"%tahun)
            else:
                print("%s bukan Tahun Kabisat"%tahun)
        else:
            print("%s merupakan Tahun Kabisat"%tahun)
    else:
        print("%s bukan Tahun Kabisat"%tahun)

print("\tLAP-YEAR CHECKER PROGRAM")
tahun= int(input("Masukkan Tahun : "))
print(Kabisat(tahun))