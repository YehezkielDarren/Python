lst=[]
lst1=[]
nama=input("Nama Pemesan >> ")
menu=input("Menu yang Diorder >> ").lower()
jumlahPesanan=int(input(f"Jumlah pesanan {menu} >> "))
lst1.append(menu), lst1.append(jumlahPesanan), lst.append(nama), lst.append(lst1)
print(lst)