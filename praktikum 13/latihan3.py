#==============================================
# Nama  : Vezilatun Nisa
# NIM   : J0403251134
# Kelas : B1
# Praktikum 13 - Graph III: Spanning Tree
#==============================================
import heapq

# Representasi weighted graph
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

# Fungsi algoritma Prim
def prim(graph, start):

    # Menyimpan node yang sudah dikunjungi
    visited = set([start])

    # Priority queue edge
    edges = []

    # Menambahkan edge awal
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    # Menyimpan hasil MST
    mst = []

    # Total bobot MST
    total_weight = 0

    # Proses Prim
    while edges:

        weight, u, v = heapq.heappop(edges)

        # Jika node belum dikunjungi
        if v not in visited:

            visited.add(v)

            mst.append((u, v, weight))

            total_weight += weight

            # Menambahkan edge baru
            for neighbor, w in graph[v].items():

                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight

# Menjalankan algoritma Prim
mst, total = prim(graph, 'A')

# Menampilkan hasil MST
print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

# Menampilkan total bobot
print("Total bobot =", total)


# ==========================================================
# Jawaban Analisis:
# 1. Node awal yang dipakai adalah node A.
#
# 2. Edge pertama yang dipilih yaitu A-C dengan bobot 2.
#
# 3. Prim memilih edge berikutnya dari node yang sudah
#    dikunjungi ke node lain dengan bobot paling kecil.
#
# 4. Total bobot MST yang dihasilkan adalah 6.
#
# 5. Bedanya Prim dan Kruskal:
#    - Prim membangun tree mulai dari satu node awal.
#    - Kruskal memilih edge dengan bobot terkecil secara global.
# ==========================================================