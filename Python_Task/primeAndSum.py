def prime():
    _range=int(input("Insert Range of Number : "))
    storage=[]

    for i in range(2,_range+1):
        _statement=True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                _statement=False
                break
        if _statement:
            storage.append(i) 
    summ=sum(storage)
    print(*storage, summ)

prime()