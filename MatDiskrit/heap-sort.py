def heapify(A, i, heap_size):
    l = left(i)
    r = right(i)
    largest = i
    if l <= heap_size and A[l - 1] > A[i - 1]:
        largest = l
    if r <= heap_size and A[r - 1] > A[largest - 1]:
        largest = r
    if largest != i:
        A[i - 1], A[largest - 1] = A[largest - 1], A[i - 1]
        heapify(A, largest, heap_size)
def build_heap(A):
    heap_size = len(A)
    for i in range(len(A) // 2, 0, -1):
        heapify(A, i, heap_size)
def heapsort(A):
    build_heap(A)
    heap_size = len(A)
    for i in range(heap_size, 1, -1):
        A[0], A[i - 1] = A[i - 1], A[0]
        heap_size -= 1
        heapify(A, 1, heap_size)
def left(i):
    return 2 * i
def right(i):
    return 2 * i + 1

# Example usage:
A = [12, 11, 13, 5, 6, 7]
heapsort(A)
print(A)