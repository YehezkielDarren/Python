#program kombinasi bilangan narsistic dan pentagon
def Range():
    #Fungsi ini untuk melakukan user input
    i = int(input("Masukkan suatu bilangan (1-999) : "))
    return i

def narsistik(bilangan_tunggal : int):
    """
  Fungsi ini memeriksa apakah bilangan_tunggal adalah bilangan narsistik.
  """
    satuan=bilangan_tunggal%10
    puluhan=(bilangan_tunggal//10)%10
    ratusan=bilangan_tunggal//100
    if bilangan_tunggal>=0:
        if bilangan_tunggal<10:
            return f"{bilangan_tunggal} :Narsistik"
        elif bilangan_tunggal<100 and bilangan_tunggal>=10:
            jumlah= satuan**2+ puluhan**2
            if jumlah==bilangan_tunggal:
                return f"{bilangan_tunggal} :Narsistik"
            else:
                return f"{bilangan_tunggal} :Bukan Narsistik"
        elif bilangan_tunggal>=100 and bilangan_tunggal<1000:
            jumlah=satuan**3+ puluhan**3+ratusan**3
            if jumlah == bilangan_tunggal:
                return f"{bilangan_tunggal} :Narsistik"
            else:
                return f"{bilangan_tunggal} :Bukan Narsistik"
    else:
        return "Di Luar Dari Ketentuan Range" 
    
def deretPentagon(sebuah_bilangan : int):
    """Fungsi ini untuk menghitung deret pentagon dari setiap bilangan dalam 
    range yang sudah diinput user""" 
    jumlah=0
    for i in range(1, sebuah_bilangan+1):
        suku=i*(3*i-1)/2 ## rumus suku ke-n = n*(3*n-1)/2
        jumlah+= suku ##menjumlahkan semua suku dalam i-range
        print(f"Suku ke-{i} -> {suku}")
    return f"Jumlah {i} suku : {jumlah}"

def main():
    print("=======================================")
    print("Program Angka Narsistik dan Pentagon")
    angka= Range()  # Assuming Range() function gets user input
    print("=======================================")
    print("Apakah termasuk Narsistik ?")
    print(narsistik(angka)) # Call narsistik and directly print the returned message
    print("=======================================")
    print(f"Suku Pentagon dari 1 sampai {angka} :")
    print(deretPentagon(angka))
    

if __name__=="__main__":
    main()