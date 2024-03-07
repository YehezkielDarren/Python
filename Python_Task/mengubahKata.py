def changeWord():
    sentence=input("Input One Sentence : ")
    sentence=sentence.lower()
    storage=""
    for i in sentence:
        if i =="a":
            storage+="i"
        elif i =="i":
            storage+="e"
        elif i=="o":
            storage+="u"
        elif i.isdigit()==True:
            storage+="@"
        else:
            storage+=i
    print(storage)

changeWord()
    