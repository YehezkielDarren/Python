def hitung_mobil():
    jumlahSol=0
    jumlahJog=0
    jumlahSur=0
    jumlahMag=0
    while True:
        masukan=input("Masukkan Asal Mobil (ketik 'Done' untuk selesai) : ")
        text=masukan.lower()
        if text == 'solo':
            jumlahSol+=1
        elif text =='magelang':
            jumlahMag+=1
        elif text=='jogja':
            jumlahJog+=1
        elif text=='surabaya':
            jumlahSur+=1
        elif text=='done':
            print(f"Jogja : {jumlahJog}\nSurabaya : {jumlahSur}\nMagelang : {jumlahMag}\nSolo : {jumlahSol}")
            break

def main():
    hitung_mobil()
    
if __name__=='__main__':
    main()
                      