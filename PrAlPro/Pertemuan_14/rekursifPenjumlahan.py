def perkalian(bil1,bil2):
    if bil2==1:
        return bil1
    else:
        return bil1+perkalian(bil1,bil2-1)
    
def perkalianfor(bil1,bil2):
    hasil=0
    for i in range(bil2):
        hasil+=bil1
    return hasil

print(perkalian(90,99))
print(perkalianfor(90,99))