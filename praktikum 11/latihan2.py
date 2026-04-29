#=======================================================
# Nama: Vezilatun Nisa
# NIM: J0403251134
#=======================================================

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

visited = set()
print("DFS dari A:")
dfs(graph, 'A', visited)


# =======================================
# Jawaban 
# =======================================

# 1. DFS masuk ke node terdalam terlebih dahulu karena
# menggunakan pendekatan rekursi atau stack,
# sehingga penelusuran dilanjutkan sampai tidak ada node baru sebelum kembali.

# 2. Jika urutan neighbor diubah,
# maka hasil DFS juga akan berubah karena urutan tersebut menentukan jalur eksplorasi.

# 3. Perbandingan DFS dan BFS:
# BFS melakukan penelusuran per level (melebar),
# sedangkan DFS menelusuri sampai kedalaman terlebih dahulu.

# Contoh:
# BFS: A B C D E F
# DFS: A B D E C F