def perkalian(bil1,bil2):
    if bil2==1:
        return bil1
    else:
        return bil1+perkalian(bil1,bil2-1)

print(perkalian(90,99))