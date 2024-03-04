#nilai kurs USD ke IDR
kursUSD = 15765

# informasi program
print("Program USD ke IDR")
print("Info Kurs USD ke IDR :\n1 USD =", kursUSD, "IDR")

#input
jumlahusd = float(input("Masukkan jumlah uang yang ditukar : "))
dalamrupiah= jumlahusd*kursUSD

# output
print("Hasil Konversi = Rp.", dalamrupiah)