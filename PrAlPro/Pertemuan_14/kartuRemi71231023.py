# def tukarRemi(n,i=1,setKartu=52):
#     if i==n:
#         tempatKartu,j=[],i
#         while j<=52:
#             tempatKartu.append(j)
#             j+=n
#         print(f"Pemain {i} : {tempatKartu}")
#     elif i<n:
#         tempatKartu,j=[],i
#         j=i
#         while j<=52:
#             tempatKartu.append(j)
#             j+=n
#         print (f"Pemain {i} : {tempatKartu}")
#         return tukarRemi(n,i+1)
        
def tukarRemi(n,i=1,setKartu=52):
    if i<=n:
        tempatKartu,j=[],i
        j=i
        while j<=52:
            tempatKartu.append(j)
            j+=n
        print (f"Pemain {i} : {tempatKartu}")
        tukarRemi(n,i+1)
pemain=int(input("Masukkan jumlah pemain : "))

tukarRemi(pemain)