#program kasir
print("PROGRAM KASIR\n\n")
#variable
kode = input("Masukkan Kode Barang : ")
nama = input("Masukkan Nama Barang : ")
harga_barang = float(input("Harga %s :" %nama))
jumlah_barang = int(input("Jumlah Barang Yang Dibeli : "))
#Proses
total_harga = harga_barang*jumlah_barang

#output
print("Kode Barang :\n%s\n\nNama Barang :\n%s\n\nHarga Satuan : %f\nJumlah Barang : %d\n\nHarga Akhir : %f" %(kode,nama,harga_barang,jumlah_barang,total_harga))
