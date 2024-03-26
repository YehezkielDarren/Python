def bubSort(lst:list):
    length=len(lst)
    for i in range(length):
        for j in range(length-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
        
    return lst

def BinarySearch(x: int,lst):
    i=0
    j=len(lst)
    while i<j:
        m=(i+j)//2
        if x>lst[m]:
            i=m+1
        else:
            j=m
    if x==lst[i]:
        return i+1
    else:
        return 0
    
def insertion(lst: list):
    n=len(lst)
    for j in range(1, n):
        i=0
        while lst[j]>lst[i]:
            i+=1
        m=lst[j]
        for k in range(j-i):
            lst[j-k]=lst[j-k-1]
        lst[i]=m
    return lst