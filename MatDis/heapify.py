def Left(i : int):
    return 2*i
def Right(i ):
    return (2*i+1)

def Heapify(A : list,i : int):
    l=Left(i)
    r=Right(i)
    if (l<=len(A)) and (A[l] and A[i]):
        largest=l
    else:
        largest=i
    if (r<=len(A)) and (A[r]>A[largest]):
        largest=r
    if largest!= i:
        A[i],A[largest]=A[largest],A[i]
        Heapify(A,largest)

def BUILD_HEAP(A):
    for i in range(len(A)/2,0):
        Heapify(A,i)

