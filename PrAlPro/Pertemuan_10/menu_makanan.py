def Pesanan(total_pesanan:list,baru:list):
    if len(total_pesanan)==0:
        total_pesanan.append(baru)
    else:
        for i in range(len(total_pesanan)):
            if total_pesanan[i][0]==baru[0]:
                if total_pesanan[i][1][0]==baru[1][0]:
                    total_pesanan[i][1][1]+=baru[1][1]
                else:
                    total_pesanan[i][1]+=baru[1]
                break
        else:
            total_pesanan.append(baru)
    return total_pesanan

def TambahMakanan():
    lst=[]
    lst1=[]
    nama=input("Nama Pemesan (Nama Lengkap) >> ")
    menu=input("Menu yang Diorder >> ").lower()
    jumlahPesanan=int(input(f"Jumlah pesanan '{menu}' >> "))
    print()
    lst1.append(menu), lst1.append(jumlahPesanan), lst.append(nama), lst.append(lst1)
    return lst #mengembalikan nilai ["nama",["menu",total pesanan]]

def MelihatPesanan(arr:list):
    print(arr)

def main():
    data_base=[]
    while True:
        print("=====================")
        print("1. Pesan Makanan")
        print("2. Melihat Pesanan")
        print("3. Exit")
        print("=====================")
        try:
            option=int(input("Pilih 1-3 >> "))
        except ValueError:
            print("Opsi Hanya Berbentuk Angka")
            continue
        else:
            if option==1:
                while True:
                    try:
                        tambah=TambahMakanan()
                        Pesanan(data_base,tambah)
                    except ValueError:
                        print("=====================")
                        print("Anda tidak mengisi semuanya, Ulangi!!")
                        print("=====================")
                    else:    
                        print("Pesanan telah di update")
                        print()
                        break
            elif option==2:
                MelihatPesanan(data_base)
            elif option==3:
                print("Terima Kasih")
                break
            else :
                print("Opsi hanya 1-3, Ulangi !!")
                continue

main()


