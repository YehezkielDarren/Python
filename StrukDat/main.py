from Single_Linked_List import NonCircular
import time

if __name__ == '__main__':
    linkedList = NonCircular()
    _i=int(input("Masukkan jumlah data : "))
    for i in range(_i):
        data=input("Masukkan Data : ")
        linkedList.insert_head(data)
    linkedList.print()
    data_recent=input("Masukkan Data Lama : ")
    data_update=input("Masukkan Data Baru : ")
    # linkedList.delete_head() -- sudah berhasil
    linkedList.update(data_recent,data_update) # sudah berhasil
    linkedList.print()
    # linkedList.delete_tail() -- sudah berhasil
    time.sleep(10)
    linkedList.delete_mid(1)
    linkedList.print()