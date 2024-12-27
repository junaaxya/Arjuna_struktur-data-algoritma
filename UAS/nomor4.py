def tambah(a,b):
    return a + b
def kurang(a,b):
    return a - b
def kali(a,b):
    return a * b
def bagi(a,b):
    if b != 0:
        return a/b
    else:
        return "EROR WOIII: PEMBAGIAN DENGAN NOL TIDAK DI BOLEHKAN YANG LAIN BE!!!!"

print("==== KALKULATOR SEDERHANA ====")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

pilihan_user = input("Pilih Pilihan Operasi yang kamu butuh (1/2/3/4) :")

try: 
    angka1 = float(input("Masukan angka pertama : "))
    angka2 = float(input("Masukan angka kedua : "))
    
    if pilihan_user == "1":
        hasil = tambah(angka1, angka2)
        print(f"hasil penjumlahan : {int(hasil)}")
    elif pilihan_user == "2":
        hasil = kurang(angka1, angka2)
        print(f"hasil pengurangan : {int(hasil)}")
    elif pilihan_user == "3":
        hasil = kali(angka1, angka2)
        print(f"hasil perkalian : {int(hasil)}")
    elif pilihan_user == "4":
        hasil = bagi(angka1, angka2)
        if isinstance(hasil, str):
            print(hasil)
        else: print(f"hasil pembagian kamu: {int(hasil)}")
        
    else:
        print("pilihan kamu tidak valid ulangi!!!!")
except ValueError:
    print("eror : masukan angka yang valid brooo")

