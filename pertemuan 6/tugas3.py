#===============================================================
# Nama   : vezilatun nisa
# NIM    : J0403251134
# Kelas  : tpl b1
#===============================================================

#===============================================================
# Latihan 3 : Tracing Insertion Sort
#===============================================================

# Fungsi insertion sort dengan tracing tiap iterasi
def insertion_sort(data):
    print("Data awal :", data)
    print("="*50)
    
    for i in range(1, len(data)):
        key = data[i]              # nilai yang akan disisipkan
        j = i - 1                  # indeks bagian kiri (yang sudah terurut)
        
        print(f"Iterasi i = {i}")
        print("Key =", key)
        
        # menghitung jumlah pergeseran pada tiap iterasi
        jumlah_geser = 0
        
        # proses pergeseran elemen yang lebih besar dari key
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
            jumlah_geser += 1
        
        # menyisipkan key ke posisi yang benar
        data[j + 1] = key
        
        print("Setelah iterasi:", data)
        print("Jumlah pergeseran:", jumlah_geser)
        print("-"*50)
    
    return data


# Data uji sesuai soal
angka = [5, 2, 4, 6, 1, 3]

print("==== Program Tracing Insertion Sort ====")
hasil = insertion_sort(angka)

print("\n===== HASIL AKHIR =====")
print("Data awal  :", [5, 2, 4, 6, 1, 3])
print("Hasil akhir:", hasil)


'''
Soal:
1. Tuliskan isi list setelah iterasi i = 1.
2. Tuliskan isi list setelah iterasi i = 3.
3. Berapa kali pergeseran terjadi pada iterasi i = 4?

Jawaban:
1. Setelah iterasi i = 1:
   [2, 5, 4, 6, 1, 3]

2. Setelah iterasi i = 3:
   [2, 4, 5, 6, 1, 3]

3. Pada iterasi i = 4 terjadi 4 kali pergeseran.
'''