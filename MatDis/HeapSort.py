import heapify as hfy

def HeapSort(A):
    for i in range(len(A),1):
        A[1],A[i]=A[i],A[1]
        heapify_sort=hfy.Heapify(A,i)
    return heapify_sort

A=[9,10,2,1,23,4,3,57,1]
print(HeapSort(A))

