n=int(input("Masukkan Jumlah Kagetori : "))
dict_aplikasi={}
for i in range(n):
    kategori=input(f"Masukkan Nama Kategori ke-{i+1} : ")
    data_apl=[]
    for i in range(5):
        nama_aplks=input(f"Masukkan Nama Aplikasi di {kategori}: ")
        data_apl.append(nama_aplks)
    dict_aplikasi[kategori]=data_apl
print(dict_aplikasi)
print()
print("Aplikasi yang berada di semua kategori")
dict_aplikasi_list=[]
for apl in dict_aplikasi.values():
    dict_aplikasi_list.append(set(apl))
print(dict_aplikasi_list)
print()
hasil=dict_aplikasi_list[0]
for i in range(1,len(dict_aplikasi_list)):
    hasil=hasil.intersection(dict_aplikasi_list[i])
print(hasil)
