print("PROGRAM TARIF TOL")

def tarif_tol(jarak, golongan):
    if golongan==1:
        tarif_tol= 10000 +((jarak-50)*1000)
    if golongan==2 :
        tarif_tol= 15000 +((jarak-50)*1500)
    if golongan==3:
        tarif_tol= 20000 +((jarak-50)*2000)
    if golongan==4:
        tarif_tol= 25000 +((jarak-50)*2500)
    return tarif_tol
def tarif(jarak):
    return 15000+((jarak-50)*1500)
        
print("RP. ", tarif_tol(150, 1))
print("RP. ",tarif_tol(golongan = 4, jarak = 200))
print("RP. ",tarif(100))