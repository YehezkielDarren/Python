import re

def cek_kodepos(kodePos):
    if len(kodePos)!=5:
        print("Tidak Valid")
    else:
        digit3=re.findall("([0-9]{3})",kodePos)
        print(digit3)
        if digit3:
            print("Tidak Valid")
        else:
            jejersama=re.findall("\d",kodePos)
            if jejersama:
                print(jejersama)
                print("Tidak Valid")
            else:
                print(jejersama)
                print("Valid")
                
cek_kodepos('12145')
cek_kodepos('32432')
cek_kodepos('55252')
cek_kodepos('55511')
cek_kodepos('55155')