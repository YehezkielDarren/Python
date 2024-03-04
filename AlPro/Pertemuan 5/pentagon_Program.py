## PROGRAM DERET PENTAGON & BILANGAN NARCISTIC
## Rumus : suku ke-n = n*(3*n-1)/2

print("DERET PENTAGON")
suku=int(input("Masukkan Banyak Suku : "))
sukuPertama= 1*(3*1-1)/2
jumlahDeret=0
for i in range(1,suku+1):
    deretPentagon=i*(3*i-1)/2
    jumlahDeret+=deretPentagon
    print(f"suku ke-{i} -> {deretPentagon}")
print("=====================================")
print(f"Jumlah {i} suku pada Deret Pentagon adalah {jumlahDeret}")


    
    

