#absolute PATH -> directory file akan fix di tempat yang sudah ditentukan walaupun code di pindah ke direktori lain
# with open("D://fruits.txt","w") as f:
#     f.write("Ayam\n")
#     f.write("Bebek\n")
#     f.write("Semangka\n")
#     f.write("Dinosaurus\n")
#     f.close()
    
#relative PATH
# with open("fruits.txt","w") as f:
#     f.write("Ayam\n")
#     f.write("Bebek\n")
#     f.write("Semangka\n")
#     f.write("Dinosaurus\n")
#     f.close()

# #MEMBACA FILE
# with open("fruits.txt","r") as f:
#         F_Readlines=f.readlines()
#         print(f"Fruit Count : {len(F_Readlines)}")
#         print(f"Fruit List : {F_Readlines}")
#         f.close()

# APPEND FILE
with open("fruits.txt","a+") as f:
    f.seek(0)
    n=int(input("Banyak tambahan list buah : "))
    for i in range(0,n):
        fruit=input("Masukkan Nama Buah : ")
        f.write(fruit+"\n")
        f.seek(0)
    fruit_list=f.readlines()
    for i in fruit_list:
        print(i.strip())
    f.close()