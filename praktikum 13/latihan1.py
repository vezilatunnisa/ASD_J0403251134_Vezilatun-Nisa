# ==========================================================
# Nama  : Vezilatun Nisa
# NIM   : J0403251134
# Kelas : B1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================

# Daftar edge graph awal
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree yang valid
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

# Menampilkan seluruh edge graph
print("Edge pada graph:")
for edge in edges:
    print(edge)

# Menampilkan spanning tree
print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

# Menampilkan jumlah edge
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))


# ==========================================================
# Jawaban Analisis:
# 1. Graph awal punya edge lebih banyak dan masih ada cycle,
#    sedangkan spanning tree cuma memakai edge yang diperlukan
#    supaya semua node tetap terhubung.
#
# 2. Spanning tree tidak boleh ada cycle karena jalurnya jadi
#    muter dan edge yang dipakai jadi berlebihan.
#
# 3. Jumlah edge spanning tree lebih sedikit karena cukup
#    memakai jumlah node - 1 edge saja.
# ==========================================================