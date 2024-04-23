def bubSort(lst:list):
    length=len(lst)
    for i in range(length):
        for j in range(length-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst
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

def BinarySearch(target: int,array : list):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def linear_search(array : list, target : int):
    for i in range(len(array)):
        if array[i]==target:
            return i 
    else:
        return -1

def max_element(numbers : list):
  maximum = numbers[0]
  for i in range(1, len(numbers)):
    if numbers[i] > maximum:
      maximum = numbers[i]
  return maximum


    

import random

def main():
    arr=[]
    n=int(input("Jumlah angka : "))
    for i in range(n):
        rand=random.randint(1,100)
        arr.append(rand)
    print(arr)
    tersusun=insertion(arr)
    print(tersusun)
    x=int(input("angka yang di cari : "))
    proposisi = "Ditemukan" if BinarySearch(x,tersusun)!=-1 else "Tidak Ditemukan"
    print(BinarySearch(x,tersusun), proposisi)
    

main()