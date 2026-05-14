#================================================
# Nama  : Vezilatun Nisa
# NIM   : J0403251134
# Kelas : B1
# Praktikum 13 - Graph III: Spanning Tree
#================================================
# Implementasi Sederhana Algoritma Kruskal
# ==========================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

# Menyimpan hasil MST
mst = []

# Menyimpan total bobot MST
total_weight = 0

# Set node yang sudah terhubung
connected = set()

# Proses algoritma Kruskal
for weight, u, v in edges:

    # Memilih edge yang tidak membentuk cycle sederhana
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
print("Total bobot =", total_weight)


# ==========================================================
# Jawaban Analisis:
# 1. Edge pertama yang dipilih adalah C-D karena bobotnya
#    paling kecil, yaitu 1.
#
# 2. Edge dengan bobot kecil dipilih lebih dulu supaya total
#    bobot MST jadi lebih minimum.
#
# 3. Total bobot MST yang dihasilkan adalah 6.
#
# 4. Ada edge yang tidak dipilih karena bisa membentuk cycle
#    atau sebenarnya sudah tidak diperlukan lagi.
# ==========================================================