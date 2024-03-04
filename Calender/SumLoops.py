def givenRange(rentang):
    total=0
    for i in range(rentang):
        total+=i
        print(total)
    return total

rentang=int(input("Masukkan Banyaka Angka : "))

print(givenRange(rentang))
        