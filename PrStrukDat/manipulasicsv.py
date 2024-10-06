with open("menu.csv","r") as f:
    _menu=f.readlines()
    for i in range(len(_menu)):
        _menu[i]=_menu[i].strip()
    
    _menu.append("Makanan;Ayam Geprek Lombok Ijo;20000")
    _menu.append("Makanan;Bebek Goreng;25000")
    _menu.append("Makanan;Sate Kambing;25000")
    _menu.append("Minuman;Es Doger;15000")

with open("menu.csv","w") as f:
    for i in _menu:
        f.write(i+"\n")
