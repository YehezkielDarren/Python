#BACA FILE CSV
# with open("test.csv","r") as csv:
#     csv_list=csv.readlines()
#     print(csv_list)
#     for i in range(1, len(csv_list)):
#         _csv=csv_list[i].strip()
#         _csv=_csv.split(",")
#         print(f"Id Pasien : {_csv[0]}")
#         print(f"Nama : {_csv[1]}")
#         print(f"Kode Jenis : {_csv[2]}")
#         print(f"Tanggal Mulai : {_csv[3]}")
#         print()
#     csv.close()
#Dengan IMPORT CSV
# import csv
# print('Data pasien berdasarkan  dan jenis kelamin')
# with open('test.csv', 'r', newline='') as datafile:
#     reader = csv.DictReader(datafile)
#     for row in reader:
#         print('ID ', row['Id Pasien'])
#         print('Nama : ', row['Nama Lengkap'])
#         print('Kode Jenis: ', row['Kode Jenis'])
#         print('Tanggal Mulai: ', row['Tanggal Mulai'])
#         print()