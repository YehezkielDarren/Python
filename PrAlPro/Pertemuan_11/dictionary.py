"""
Python built-in function
=============================
clear()         Removes all the elements from the dictionary
copy()          Returns a copy of the dictionary
fromkeys()      Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items()     	Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary
"""
dictionary={    #tipe data dictionary data menampung jenis tipe data yang berbeda
    "nama_buku":"Calistung Edisi 2024", #key : value
    "Tahun_terbit" : 2024,
    "Penerbit":"Erlangga",
    "Penulis":"Ucup"
}
#mengecek tipe data
for key,value in dictionary.items():
    print(f"{key} : ",type(key))
    print(f"{value} : ",type(value))
print()
for i in dictionary:
    print(i, ":",dictionary[i]) # output i sebagai keys, output dictionary[i] sebagai values
print()
for keys,values in dictionary.items():
    print(f"{keys} : {values}")
print()
# get() function
print(dictionary.get("Penulis"))
print("===============================")
#Nested dicitionary
user1={
    "nama" : "ndus",
    "umur" : 99,
    "jenis_kelamin": "attack_helicopter",
}
user2={
    "nama" : "ganjar",
    "umur" : 16,
    "jenis_kelamin": "pria",
}
user3={
    "nama" : "wowok",
    "umur" : 42,
    "jenis_kelamin": "mk",
}
dataBase={
    "data1" : user1,
    "data2":user2,
    "data3":user3
}
print(dataBase) #acces all items
for i in dataBase.values(): #accesing values of dictionary
    print(i)
    for j in i.items(): #accessing keys and values
        print(j)
    print()
