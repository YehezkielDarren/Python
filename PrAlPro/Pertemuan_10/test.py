seconds=129
time=[]
minute=seconds//60
second=seconds%60
hours=minute//60
print(f"{hours} hours : {minute} : {second}")
#mencari hasil bagi
while seconds != 60:
    temp=""
    x=seconds//60
    y=seconds
    