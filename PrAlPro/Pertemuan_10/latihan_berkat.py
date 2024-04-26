# def anagram(arr : list): #cara pake count
#     anagram_=[]
#     tidak_anagram=[]
#     for i in range(len(arr)):
#         count=0
#         for j in range(len(arr)):
#             if sorted(arr[i]) == sorted(arr[j]):
#                 count+=1
#         if count>1:
#             anagram_.append(arr[i])
#         else:
#             tidak_anagram.append(arr[i])
#     if anagram_==[] and tidak_anagram!=[]:
#         return [tidak_anagram]
#     elif anagram_!=[] and tidak_anagram==[]:
#         return [anagram_]
#     elif anagram_!=[] and tidak_anagram!=[]:
#         return [anagram_, tidak_anagram]

def anagram(arr : list): #cara pake algoritma bilangan prima
    ini_anagram=[]
    bukan_anagram=[]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if sorted(arr[i]) == sorted(arr[j]):
                ini_anagram.append(arr[i])
                break
        else:
            bukan_anagram.append(arr[i])
    if ini_anagram==[] and bukan_anagram!=[]:
        return [bukan_anagram]
    elif ini_anagram!=[] and bukan_anagram==[]:
        return [ini_anagram]
    elif ini_anagram!=[] and bukan_anagram!=[]:
        return [ini_anagram,bukan_anagram]
print(anagram(["ate","tea", "eat","tan","dawn"]))
print(anagram(["cinema","iceman"]))
print(anagram(["hello","world","elloh"]))
print(anagram(["stop","pots","tops"]))
print(anagram(["ayam","maya","yama","ikan"]))
print(anagram(["ivan","vani","niva","avan","vana"]))
