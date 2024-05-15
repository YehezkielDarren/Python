direktori=dict()
for _ in range(2):
    first=input("Nama pertama >> ")
    last=input("Nama terakhir >> ")
    number=input("Nomor telepon Anda >> ")
    direktori[first,last]=number
for keys,vals in direktori:
    print((keys,vals), direktori[keys,vals])