listKota = ['jakarta', 'banyuwangi', 'bangka belitung', 'semarang', 'tanggerang', 'surabaya']

# # for kota in listKota:
# #     if 'jakarta' in listKota:
# #         print('ada')
# #     else:
# #         print('tidak ada')

# # for a in range(10):
# #     print('perulanga ke - ', a + 1)
    
# for ganjil in range(1,100):
#     if ganjil % 2 == 1:
#         print(ganjil)

# for kota in listKota :
#     print(kota)
# else: 
#     print('tidak ada list kota')

kotayangkamucari= input("masukan kota yang kamu cari : ")

for index, kota in enumerate(listKota):
    if kota.lower() == kotayangkamucari.lower():
        print(f"{index} : {kota}")