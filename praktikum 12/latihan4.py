#===========================================================
# Nama  : vezilatun nisa
# NIM   : J0403251134
# Kelas : B1
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================

import heapq

graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


hasil = dijkstra(graph, 'Gerbang')

print("Jarak terpendek dari Gerbang:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")


# Jawaban Analisis:

# 1. Yang paling dekat dari Gerbang itu Kantin (2 menit)

# 2. Waktu tercepat ke Aula:
#    lewat Gerbang -> Kantin -> Lab -> Aula
#    totalnya 2 + 4 + 1 = 7 menit

# 3. tidak selalu.
#    Kadang jalur langsung malah lebih lama dibanding lewat beberapa tempat

# 4. Karena semua bobotnya positif (waktu tempuh),
#    jadi Dijkstra aman dipakai di kasus ini