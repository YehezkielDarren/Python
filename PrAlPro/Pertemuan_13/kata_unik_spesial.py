def kata_unik_spesial(kalimat1:str,kalimat2:str)-> set:
    kalimat1, kalimat2= kalimat1.split(), kalimat2.split()
    cek_duplikat,hasil=dict(),list()
    for word1 in (kalimat1):
        if word1 not in cek_duplikat.keys():
            hasil.append(word1)
            cek_duplikat[word1]=cek_duplikat.get(word1,0)+1
        else:
            if cek_duplikat[word1]<2:
                hasil[hasil.index(word1)]+=word1
                cek_duplikat[word1]=cek_duplikat.get(word1,0)+1
    for word2 in  kalimat2:
        if word2 not in cek_duplikat.keys():
            hasil.append(word2)
            cek_duplikat[word2]=cek_duplikat.get(word2,0)+1
        else:
            if cek_duplikat[word2]<2:
                hasil[hasil.index(word2)]+=word2
                cek_duplikat[word2]=cek_duplikat.get(word2,0)+1
    return set(hasil)

def kataUnik_spesial(kalimat1,kalimat2):
    kalimat1,kalimat2,hasil=kalimat1.split(),kalimat2.split(),[]
    for word in (kalimat1+kalimat2):
        if (kalimat1+kalimat2).count(word)>1:
            hasil.append(word+word)
        else:
            hasil.append(word)
    return set(hasil)
        

result=kata_unik_spesial("saya mau mandi saya mau makan","ndus mau ngising")
result1=kataUnik_spesial("saya mau mandi saya mau makan","ndus mau ngising")
print(len(result))
print(sorted(result))
print(len(result1))
print(sorted(result1))
        
result=kata_unik_spesial("saya mau makan dan mau mandi","saya main sepak bola")
result1=kataUnik_spesial("saya mau makan dan mau mandi","saya main sepak bola")
print(len(result))
print(sorted(result))
print(len(result1))
print(sorted(result1))
        