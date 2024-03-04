sebuahBilangan=int(input("Maksimal Range (1-999):"))
for i in range(1, sebuahBilangan+1):
    satuanBil=i%10
    puluhanBil=(i//10)%10
    ratusanBil=i//100
    if i >=0 and i <10:
        print(f"{i} : bilangan narsis")
    elif i<100:
        eksponen = 2
        narsis= satuanBil**eksponen+puluhanBil**eksponen
        if narsis==i:
            print(f"{i} : bilangan narsis")
        else :
            print(f"{i} : bukan bilangan narsis") 
    elif i<1000:
        eksponen=3
        narsis= satuanBil**eksponen+puluhanBil**eksponen
        if narsis==i:
            print(f"{i} : bilangan narsis")
        else :
            print(f"{i} : bukan bilangan narsis") 
    else :
        print("Sudah melebihi range")
        break