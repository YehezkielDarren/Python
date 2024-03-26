import Matdis
import random as rnd

def main():
    arr=[]
    banyakAngka=int(input("masukkan banyaknya angka yang akan digenerate acak : "))
    for _ in range(banyakAngka):
        x=rnd.randint(1,100)
        while x in arr:
            x=rnd.randint(1,100)
        arr.append(x)
    target=int(input("What's your target? "))
    sort=Matdis.insertion(arr)
    search=Matdis.BinarySearch(target,sort)
    print(f"Array setelah diurutkan:\n{sort}")
    if search!=0:
        print(f"Bilangan {target} ada di indeks ke {search} ")
    else:
        print(f"Bilangan {target} tidak ada di array")
        
main()
    


