def sortinglist(arr : list):
    lst=[]
    for i in arr:
        if type(i)==list:
            for y in i:
                lst.append(y)
        elif type(i)==int:
            lst.append(i)
    lst.sort(reverse=True)
    return "~"+"~".join(str(i) for i in lst)+"~"

print(sortinglist([9,7,6,"ayam",[1,5,2],8]))
                