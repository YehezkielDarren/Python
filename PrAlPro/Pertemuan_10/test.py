def BigThree(n:list):
    n.sort(reverse=True)
    return n[:3]
#Cara Cepat, tapi hanya untuk data int dan bukan untuk list dalam list

print(BigThree([9,0,1,3,4,-1,10]))