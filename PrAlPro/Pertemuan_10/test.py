def BigThree(angka:list):
    angka.sort(reverse=True)
    return angka[:3]
print(BigThree([9,0,1,3,4,-1,10]))