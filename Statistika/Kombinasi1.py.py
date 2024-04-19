
teman_ibu=["Sandra","Susi","Maria","Lina","Rita"]
kombinasi_total=[]
for i in range(len(teman_ibu)):
    for y in range(i+1,len(teman_ibu)):
        for z in range(y+1, len(teman_ibu)):
            kombinasi=[teman_ibu[i],teman_ibu[y],teman_ibu[z]]
            if kombinasi not in kombinasi_total:
                kombinasi_total.append(kombinasi)

print(kombinasi_total, len(kombinasi_total))
