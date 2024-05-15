import string

try:
    handle=open("contoh1.txt")
    handle=handle.readlines()
except FileNotFoundError:
    print("File not found")
counts=dict()
for line in handle[:5]:
    line=line.translate(str.maketrans("","",string.punctuation))
    words=line.lower().split()
    for word in words:
        counts[word]=counts.get(word,0)+1
print(counts)
print()
lst=list()
for key,val in counts.items():
    if val%2==0:
        lst.append((key,val))
print(lst)