def hitung_gaji_karyawan(tarif_perjam, jamKerja_harian, hari_kerja):
    total_gaji = 0
    jam_normal = 0 
    
    for hari in range(1, hari_kerja + 1):
        if jamKerja_harian[hari - 1] > jam_normal:
            jam_lembur = jamKerja_harian[hari - 1] - jam_normal
            gaji_harian =(jam_normal * tarif_perjam) + (jam_lembur * tarif_perjam * 1.5)
        else:
            gaji_harian = jamKerja_harian[hari - 1] * tarif_perjam
            
        total_gaji += gaji_harian
        
    return total_gaji
    
tarif_perjam = float(input("masukan tarif gaji perjam : "))
hari_kerja = int(input(" masukan jumlah hari kerja dalam sebulan : "))

jamKerja_harian = []
for hari in range(1, hari_kerja + 1):
    jam_kerja = float(input(f"masukan jam kerja pada hari ke-{hari} :"))
    jamKerja_harian.append(jam_kerja)
        
total_gaji_bulanan = hitung_gaji_karyawan(tarif_perjam, jamKerja_harian, hari_kerja)
print(f"\nTotal gaji bulanan adalah: Rp{total_gaji_bulanan:,.2f}")
    