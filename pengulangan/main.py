# while (1+4 == 5):
#     print("hello dunia")
#     break

# listkota =['jakarta','bangka belitung', 'banyuwangi', 'semarang','bali', 'labuan bajo','permis', 'kapung anyar']
# i = 0

# while i < len(listkota):
#     print(listkota[i])
#     i += 1
    
a = int(input('Masukan angka terserah kamu: '))

while a % 2 == 0 or a <= 50:  
    print('SALAH')
    a = int(input('Masukkan lagi: '))  

print("BENAR", a)