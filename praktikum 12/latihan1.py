#=========================================================
# Nama  : Vezilatun Nisa
# NIM   : J0403251134
# Kelas : B1
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================

# Representasi weighted graph
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Hitung jalur
jalur_1 = graph['A']['B'] + graph['B']['D']   # A -> B -> D
jalur_2 = graph['A']['C'] + graph['C']['D']   # A -> C -> D

print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")


# Jawaban Analisis:

# 1. Total bobot jalur A -> B -> D = 4 + 5 = 9
# 2. Total bobot jalur A -> C -> D = 2 + 1 = 3
# 3. Jalur terpendek adalah A -> C -> D
# 4. Karena shortest path ditentukan dari total bobot terkecil,
#    bukan dari jumlah edge. Meskipun jumlah edge sama,
#    bobotnya bisa berbeda.