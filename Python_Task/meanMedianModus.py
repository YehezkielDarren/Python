import statistics

"""Fungsi Inputan"""

def inputan():
    data=[]
    masukkan_data=input("Masukkan Integer Positif (PISAHKAN DENGAN KOMA): ")
    for i in masukkan_data.split(','):
        data.append(int(i))
    return data

def inputanSorted(bilangan):
    bilangan=sorted(bilangan)
    return bilangan

"""Fungsi Menghitung Median"""
def mean(bilangan):
    return sum(bilangan)/len(bilangan)

def median(bilangan):
    inputanSorted(bilangan)
    panjang=len(bilangan)
    titik_tengah=panjang//2
    if panjang%2!=0:
        return bilangan[titik_tengah+1]
    else :
        return (bilangan[titik_tengah]+bilangan[titik_tengah+1])/2

"""Fungsi Mencari Modus"""
def modus(bilangan):
    modus = statistics.mode(bilangan)
    return modus

def main():
    print("------Data------")
    temp=inputan()
    print("================")
    print("Isi data yang telah di susun : ", inputanSorted(temp))
    print("================")
    print("Rata-rata data : ",mean(temp))
    print("================")
    print("Titik tengah data : ",median(temp))
    print("================")
    print("Modus data : ",modus(temp))

if __name__ =="__main__":
    main()
