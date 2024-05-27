def faktorialgenap(jumlah,awal):
    if jumlah == 0:
        return 1
    return 1*faktorialgenap(jumlah,awal+2) if awal ==0 else awal * faktorialgenap(jumlah - 1, awal+2)


print(faktorialgenap(5,0))
print(faktorialgenap(2,0))
print(faktorialgenap(10,0))
print(faktorialgenap(5, 0))
print(faktorialgenap(2, 2))
print(faktorialgenap(10, 2))