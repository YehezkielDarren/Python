"""Fungsi Inputan"""

def inputan():
    data=[]
    masukkan_data=input("Masukkan Integer Positif (PISAHKAN DENGAN KOMA): ")
    for i in masukkan_data.split(','):
        data.append(int(i))
    return data[i]

"""Fungsi Menghitung Median"""
def mean(bilangan):
    return sum(bilangan)/len(bilangan)

def median(bilangan):
    bilangan=sorted()
    titik_tengah=len(bilangan)
    if titik_tengah%2!=0:
        return bilangan[titik_tengah]
    else :
        return (bilangan[titik_tengah-1]+bilangan[titik_tengah+1])/2

"""Fungsi Mencari Modus"""
def modus(bilangan):
    pass

def main():
    pass

if __name__ =="__main__":
    main()