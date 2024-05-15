t1=9,9,18
print(t1==t1)
for i in range(len(t1)):
    if t1[i%len(t1)]!=t1[i+1]:
        print(False)
        break
else:
    print(True)
