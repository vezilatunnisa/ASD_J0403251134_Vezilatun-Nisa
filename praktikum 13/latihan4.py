#=====================================================
# Nama  : Vezilatun Nisa
# NIM   : J0403251134
# Kelas : B1
# Praktikum 13 - Graph III: Spanning Tree
#=====================================================
# Studi kasus jaringan kabel antar gedung
# Menggunakan algoritma Kruskal
# Daftar edge graph
edges = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
]

# Mengurutkan edge berdasarkan bobot
edges.sort()

# Menyimpan hasil MST
mst = []

# Menyimpan total biaya minimum
total_cost = 0

# Menyimpan node yang sudah terhubung
connected = set()

# Proses Kruskal
for weight, u, v in edges:

    # Memilih edge yang tidak membentuk cycle
    if u not in connected or v not in connected:

        mst.append((u, v, weight))

        total_cost += weight

        connected.add(u)
        connected.add(v)

# Menampilkan hasil MST
print("Jaringan Kabel Minimum:")

for edge in mst:
    print(edge)

# Menampilkan total biaya minimum
print("Total biaya minimum =", total_cost)


# ==========================================================
# Jawaban Analisis:
# 1. Algoritma yang dipakai adalah algoritma Kruskal.
#
# 2. Edge yang dipilih yaitu:
#    - GedungC - GedungD = 1
#    - GedungA - GedungC = 2
#    - GedungB - GedungD = 3
#
# 3. Total biaya minimum yang didapat adalah 6.
#
# 4. MST cocok dipakai pada kasus ini karena semua gedung
#    bisa tetap terhubung dengan biaya kabel yang lebih hemat.
# ==========================================================