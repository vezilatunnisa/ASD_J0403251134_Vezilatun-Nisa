#==================================================================
# Nama: Vezilatun Nisa
# NIM: J0403251134
#==================================================================

from collections import deque

graph = {
    'Rumah': ['Sekolah', 'Toko'],
    'Sekolah': ['Perpustakaan'],
    'Toko': ['Pasar'],
    'Perpustakaan': [],
    'Pasar': []
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

print("BFS dari Rumah:")
bfs(graph, 'Rumah')


# =======================================
# Jawaban 
# =======================================

# 1. Node pertama yang dikunjungi adalah "Rumah"
# karena BFS selalu dimulai dari node awal (start).

# 2. BFS cocok untuk mencari jalur terdekat karena
# proses penelusurannya dilakukan per level,
# sehingga node yang jaraknya paling dekat akan dikunjungi lebih dulu.

# 3. Jika struktur graph diubah,
# maka urutan BFS juga dapat berubah karena BFS mengikuti urutan neighbor.
# Jadi susunan tetangga dalam graph mempengaruhi hasil traversal.