import statistics

"""Fungsi Inputan"""

def inputan():
    data=[]
    masukkan_data=input("Masukkan Integer Positif (PISAHKAN DENGAN KOMA): ")
    for i in masukkan_data.split(','):
        data.append(int(i))
    return data

"""Fungsi Menghitung Median"""
def mean(bilangan):
    return sum(bilangan)/len(bilangan)

def median(bilangan):
    bilangan=bilangan.sort()
    titik_tengah=len(bilangan)
    if titik_tengah%2!=0:
        return bilangan[titik_tengah]
    else :
        return (bilangan[titik_tengah-1]+bilangan[titik_tengah+1])/2

"""Fungsi Mencari Modus"""
def modus(bilangan):
    modus = statistics.mode(bilangan)
    return modus

def main():
    print("------Data------")
    temp=inputan()
    mean(temp)
    median(temp)
    modus(temp)

if __name__ =="__main__":
    main()
