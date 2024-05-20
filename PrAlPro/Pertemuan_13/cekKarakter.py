def cekKarakter(kalimat):
    kalimat=kalimat.lower().split()
    cek=set()
    for word in kalimat:
        for char in word:
            cek.add(char)
    if len(cek)==26:
        print("Kalimat ini memiliki semua alfabet")
    else:
        print("Kalimat ini tidak memiliki semua alfabet")
        
cekKarakter("A quick brown fox jumps over the lazy dog")
cekKarakter("A quick brown fox jumps over the lazy cat")

        