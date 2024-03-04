#Jumlah emas awal yang dibeli
Goldfirst_gram = 25

#Harga beli awal
Goldprice_first = 650000
#Kenaikan harga pertama
Goldprice_second= 685000

#Perhitungan
Buy_first = Goldfirst_gram*Goldprice_first
Sell_first = Goldfirst_gram*Goldprice_second

#Keuntungan (Dalam Rp. dan % )
Profit = Sell_first - Buy_first
Percentage = float((Profit/Buy_first)*100)

print("Keuntungan yang didapat Gerrad adalah Rp. ",Profit)
print("Persentase Keuntungannya adalah ",Percentage,"%")

