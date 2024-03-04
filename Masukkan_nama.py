def inputName(banyaknya):
    names=[]
    for i in range(1,banyaknya+1):
        insert= str(input(f"{i}. Masukkan nama : "))
        names.append(insert)
    return names

def callName(banyaknya):
    for i in banyaknya:
        print(i)
        

def main():
    jumlah = int(input("Masukkan Jumlah Data : "))
    ini_masuk = inputName(jumlah)
    print("Daftar nama : ")
    callName(ini_masuk)
    

if __name__ =="__main__":
    main()