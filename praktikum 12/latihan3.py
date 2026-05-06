#===========================================================
# Nama  : Vezilatun Nisa
# NIM   : J0403251134
# Kelas : B1
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================

graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances


hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)


# Jawaban Analisis:
# 1. Bobot langsung dari A ke B itu 5
# 2. Total bobot A -> C -> B = 4 + (-2) = 2
# 3. Jalur yang paling bagus itu A -> C -> B karena lebih kecil (2)
# 4. Karena Bellman-Ford ngecek semua edge berkali-kali,
#    jadi dia tetap bisa nemuin hasil yang benar walaupun ada bobot negatif
# 5. Relaksasi edge itu maksudnya nge-update jarak
#    kalau ketemu jalur yang lebih kecil
# 6. Perbedaannya:
#    - Dijkstra: lebih cepat, tapi nggak bisa handle bobot negatif
#    - Bellman-Ford: lebih lambat, tapi bisa handle bobot negatif