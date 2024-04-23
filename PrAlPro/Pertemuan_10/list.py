def appendData():
    list_temp=[]
    nomor_ID=""
    print("Silahkan masukkan data yang diperlukan\n")
    nama=input("Silahkan masukkan nama lengkap anda\n>>").split()
    lahir=input("Silahkan masukkan tanggal lahir (Format :'DD-MM-YY')\n>>").split("-")
    nomor_ID+=lahir[1]
    for i in range(len(nama)):
        if i%2!=0:
            continue
        else:
            nomor_ID+=nama[i][0]
    list_temp.append(nomor_ID)
    list_temp.append(nama)
    list_temp.append(lahir)
    return list_temp

def readData(arr):
    for i in arr:
        print("Nomor ID >>", i[0])
        print("Nama Lengkap >>", i[1])
        print("Nama Depan >>", i[1][0])
        print("Nama Belakang >>", i[1][-1])
        print("Tanggal Lahir >>", i[2][0])
        print("Bulan Lahir >>", i[2][1])
        print("Tahun Lahir >>", i[2][2])
        print(i)


    

def main():
    arr=[]
    yes_no=['Y','N']
    while True:
        print("1. Menambah Data")
        print("2. Melihat Data")
        print("3. Exit")
        try:
            inpt=int(input("Masukkan Pilihan : "))
        except ValueError:
            print()
            print("Silahkan Masukkan Pilihan Berupa Angka")
            print()
            continue
        else:
            if inpt<1 and inpt>3:
                print("Pilihan hanya dari 1-3")
                continue
        if inpt==1:
            hasil=appendData()
            arr.append(hasil)
            
        elif inpt==2:
            readData(hasil)
            
        else:
            print("Terima kasih")
            break

main()