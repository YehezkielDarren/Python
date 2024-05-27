def eksponen(bil,n):
    if n==1:
        return bil
    return bil*eksponen(bil,n-1)

print(eksponen(2,3))