#=========================================================
# Nama  : Vezilatun Nisa
# NIM   : J0403251134
# Kelas : B1
# Praktikum 12 - Graph II: Shortest Path
#==========================================================
# Latihan 5: Jalur Kota
#==========================================================
import heapq

graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
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


hasil = dijkstra(graph, 'Bogor')

print("Jarak terpendek dari Bogor:")
for kota, jarak in hasil.items():
    print("Bogor ->", kota, "=", jarak)


# Jawaban Analisis:
# 1. Bogor
# 2. Depok (2)
# 3. Bandung (8)
# 4. Dijkstra memilih jarak terkecil dulu lalu update node lain