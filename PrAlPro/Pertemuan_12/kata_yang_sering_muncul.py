import string
with open("danau-toba.txt") as f:
    handle=f.readlines()
counts=dict()
for line in handle:
    line=line.translate(str.maketrans("","",string.punctuation))
    words=line.rstrip().lower().split()
    for word in words:
        counts[word]=counts.get(word,0)+1
lst=list()
for key,val in counts.items():
    lst.append((val,key))
lst.sort(reverse=True)
for key,value in lst[:10]:
    print(key,value)