def appendData():
    list_temp=[]
    nomor_ID=""
    print("Silahkan masukkan data yang diperlukan\n")
    nama=input("Silahkan masukkan nama lengkap anda\n>>").split()
    print()
    lahir=input("Silahkan masukkan tanggal lahir (Format :'DD-MM-YY')\n>>").split("-")
    print()
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
    for i in range(len(arr)):
        print(arr[i])


    

def main():
    yes_no=['Y','N']
    while True:
        arr=[]
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
        if inpt==1:
            while True:
                hasil=appendData()
                arr.append(hasil)
                yesNo=input("Apakah ingin lanjut ? (Y/N) ").upper()
                if yesNo==yes_no[0]:
                    continue
                else:
                    break
            
        elif inpt==2:
            readData(hasil)
        elif inpt==3:
            print("Terima kasih")
            break
        else:
            print("Pilihan yang tersedia hanya 1-3.\n")
            continue

main()