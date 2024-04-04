def koversiHurufAngka(n:str):
    n=n.lower()
    hasil="-".join(str(ord(i)-96) for i in n if i.isalpha())
    return hasil

def simbolBerlebih(string :str):
    n=n.lower()
    hasil=""
    for i in range(len(string)):
        count=0
        for j in range(len(string)):
            if string[i]==string[j]:
                count+=1
        if count>1:
           hasil+=">"
        else:
            hasil+="<" 
    return hasil

def prima(bawah:int, atas: int)-> list:
    if bawah<=2:
        hasil=""
        for i in range(2,atas+1):
            for j in range(2, int(i**0.5)+1):
                if i%j==0:
                    break
            else:
                hasil+=str(i)+" "
        return hasil
    elif bawah>2:
        hasil=""
        for i in range(bawah,atas+1):
            for j in range(2, int(i**0.5)+1):
                if i%j==0:
                    break
            else:
                hasil+=str(i)+" "
        return hasil
    
def countPrima(n :str)-> int:
    count=0
    n=n.split()
    for _ in n:
        count+=1
    return count

def hapusduplikatberurutan(kata):
    kata=kata.lower()
    hasil=kata[0]
    for i in range(1,len(kata)):
        if kata[i]!=kata[i-1]:
            hasil+=kata[i]
        else:
            continue
    return hasil

def main():
    print("=============================")
    print("1. Konversi Huruf Angka")
    print("2. Konversi Simbol Berlebih")
    print("3. Kemunculan Prima")
    print("4. Hapus Duplikat Berurutan")
    print("=============================")
    option=int(input("Nomor mana yang dipilih : "))
    if option == 1:
        print("--Konversi Huruf Angka--")
        huruf=input("Masukkan Sebuah Kata : ")
        print(f"Hasil : {koversiHurufAngka(huruf)}")
    elif option==2:
        print("--Konversi Simbol Berlebih--")
        huruf=input("Masukkan Sebuah Kata : ")
        print(f"Hasil : {simbolBerlebih(huruf)}")
    elif option==3:
        print("--Kemunculan Prima--")
        batasBawah=int(input("Masukkan Batas Bawah : "))
        batasAtas=int(input("Masukkan Batas Atas : "))
        hasil=prima(batasBawah,batasAtas)
        print(f"Bilangan Prima : {hasil}\nJumlah Kemunculan Bilangan Prima Sebanyak {countPrima(hasil)} x")
    elif option==4:
        print("--Hapus Duplikat Berurutan--")
        huruf=input("Masukkan Sebuah Kata : ")
        print(f"Hasil : {hapusduplikatberurutan(huruf)}")
        
main()
        
        