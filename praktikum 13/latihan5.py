#==================================
# Nama  : Vezilatun Nisa
# NIM   : J0403251134
# Kelas : B1
# Praktikum 13 - Graph III: Spanning Tree
#==================================
# Kasus yang dipilih:
# Jaringan Jalan Antar Kota

# Daftar edge graph
edges = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

# Menyimpan hasil MST
mst = []

# Menyimpan total bobot MST
total_weight = 0

# Menyimpan node yang sudah terhubung
connected = set()

# Proses algoritma Kruskal
for weight, u, v in edges:

    # Memilih edge yang tidak membentuk cycle
    if u not in connected or v not in connected:

        mst.append((u, v, weight))

        total_weight += weight

        connected.add(u)
        connected.add(v)

# Menampilkan hasil MST
print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

# Menampilkan total bobot
print("Total bobot MST =", total_weight)


# ==========================================================
# Jawaban Analisis:
# 1. Kasus yang dipilih adalah jaringan jalan antar kota.
#
# 2. Algoritma yang dipakai adalah algoritma Kruskal.
#
# 3. Edge yang masuk ke MST yaitu:
#    - Bogor - Depok = 2
#    - Depok - Jakarta = 3
#    - Depok - Bandung = 4
#
# 4. Total bobot MST yang didapat adalah 9.
#
# 5. Ada edge yang tidak dipilih karena bisa membentuk
#    cycle atau bobotnya lebih besar dibanding edge lain.
# ==========================================================