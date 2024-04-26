def setengah_reverse(kalimat:str):
    kalimat=kalimat.split()
    awal,akhir=[],[]
    for i in range(len(kalimat)):
        if i >= int(len(kalimat)//2):
            akhir.append(kalimat[i])
        else:
            awal.append(kalimat[i])
    a,b,jawaban=-1,0,[] #a untuk indeks awal dan b untuk indeks akhir
    for i in range(len(awal)+len(akhir)):
        if i %2==0:
            jawaban.append(akhir[b])
            b+=1
        else:
            jawaban.append(awal[a][-1::-1])
            a-=1
    return " ".join((jawaban))

print(setengah_reverse("ayam berkokok di siang hari"))
print(setengah_reverse("UKDW memiliki fakultas teknologi informasi yang terdiri dari prodi informatika dan sistem informasi"))
