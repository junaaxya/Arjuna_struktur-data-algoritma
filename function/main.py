# def assalamualaikum():
#     print('assalamualiku  brthoer')
    
# assalamualaikum()

# def luasSegitiga(alas, tinggi):
#     luas =(alas * tinggi) / 2
#     print(f"luas segita : {luas:.2f}")

# luasSegitiga(5,7)

# def luaspersegi(sisi):
#     luas = sisi * sisi
#     print(f'luas persegi adalah {luas}')

# luaspersegi(6)

# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas

# def volume_persegi(sisi):
#     volume= luas_persegi(sisi) * sisi
#     return volume


# sisi = int(input("masukan angka bilangan bulat: "))
# volume = volume_persegi(sisi)

# print(f"volume kubus dengan {sisi} adalah {volume}")

buku = ['buku ipa','buku bahasa','buku komik']
def show_data():
    if not buku:
        print("Belum ada data")
    else:
        for indeks, item in enumerate(buku):
            print(f'[{indeks}] {item}')

def insert_data():
    buku.append(input('masukan judul buku yang ingin di masukan: '))

def edit_data():
    show_data()
    try:
        indeks = int(input('input id buku: '))
        if 0 <= indeks < len(buku):
            buku[indeks ] = input("masukan judul baru: ")
        else:
            print('id salah')       
    except ValueError:
        print('harap masukan angka yang valid')
        
def delete_data():
    show_data()
    try:
        indeks = int(input('Input ID buku yang ingin dihapus: '))
        if 0 <= indeks < len(buku):
            buku.pop(indeks)
            print("Data berhasil dihapus")
        else:
            print("ID salah")
    except ValueError:
        print("Harap masukkan angka yang valid")
        
        
def menu():
    print("\n")
    print("---------menu---------")
    print("[1] show data")
    print("[2] insert data")
    print("[3] edit data")
    print("[4] delete data")
    print("[5] exit")
    
    menu = int(input('pilih menu: '))
    if int(menu) == 1:
        show_data()
    elif int(menu) == 2:
        insert_data()
    elif int(menu) == 3:
        edit_data() 
    elif int(menu) == 4:
        delete_data() 
    elif int(menu) == 5:
        exit() 
    else:
        print("salah pilih") 
        
def main():
    buku = []
    while True:
        menu()
        
main()
        