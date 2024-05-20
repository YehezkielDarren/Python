n=int(input("Masukkan Jumlah Kagetori : "))
dict_aplikasi={}
for i in range(n):
    kategori=input(f"Masukkan Nama Kategori ke-{i+1} : ")
    data_apl=[]
    for i in range(5):
        nama_aplks=input(f"Masukkan Nama Aplikasi di {kategori}: ")
        data_apl.append(nama_aplks)
    dict_aplikasi[kategori]=set(data_apl)
listTuple=list()
for key,val in dict_aplikasi.items():
    listTuple.append((key, val))
if n==2:
    for i in range(len(listTuple)):
        print(f"{listTuple[i][0]} : {listTuple[i][1]-listTuple[(i+1)%len(listTuple)][1]}")
elif n>2:
    for i in range(len(listTuple)):
        print(f"{listTuple[i][0]} : {listTuple[i][1]^listTuple[(i+1)%len(listTuple)][1]}")