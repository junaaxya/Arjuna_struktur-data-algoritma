# print("kode program ini akan di eksekusi") if True else print('ini tidak akan di eksekusi')

# a = input("masukan angka 1- 10 :" )
# b = input("masukan angka 1-10 :")

# print(f"nilai yang kamu masukan pertama: {int(a)}")
# print(f"nilai yang kamu masukan kedua: {int(b)}")

# if a > b :
#     print("lebih besar a", int(a))
# elif b > a: 
#     print("lebih besar b", int(b))
    
# name = input("masukan nama kamu : ")

# if name == "steven":
#     print("selamat datang steven")
# else: 
#     print("kamu bukan steven pergi saja!!!!")
    
# nilai = int(input("masukan nilai anda : "))

# Predika_A = nilai > 90
# Predika_B = nilai > 80
# Predika_C = nilai > 70 
# Predika_D = nilai > 60

# if Predika_A :
#     print(" nilai anda adalah a")
# elif Predika_B : 
#     print("Nilai anda adalah b")
# elif Predika_C : 
#     print("Nialai anda c")
# elif Predika_D :
#     print(" nilai anda D")
# else:
#     print("kamu tidak lulus")
    
list_buah = ["mangga","mengkudu","nanas","apel"]
list_buah_dicari = input("masukan nama buah yang akan kamu cari :")

if list_buah_dicari in list_buah :
    print(f"buah yang kamu cari ada{list_buah_dicari}")
else:
    print("buah yang kamu cari tidak ada")