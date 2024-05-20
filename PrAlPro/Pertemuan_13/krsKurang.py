def krsKurang(lst1,lst2):
    lst1,lst2=set(lst1),set(lst2)
    print(len(lst1-lst2))