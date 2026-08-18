# ==========================
# ALGORITMO BELLMAN-FORD
# ==========================
def bellman_ford(vertices, arestas, origem):
    # Inicializa distâncias
    distancias = {}
    for v in vertices:
        distancias[v] = float('inf')
    distancias[origem] = 0
    # Relaxamento das arestas
    for i in range(len(vertices) - 1):
        for u, v, peso in arestas:
            if distancias[u] != float('inf') and distancias[u] + peso < distancias[v]:
                distancias[v] = distancias[u] + peso
    # Verifica ciclo negativo
    for u, v, peso in arestas:
        if distancias[u] != float('inf') and distancias[u] + peso < distancias[v]:
            print("\nO grafo possui ciclo negativo!")
            return None
    return distancias

# ==========================
# ENTRADA DE DADOS
# ==========================
vertices = []
arestas = []

qtd_vertices = int(input("Quantidade de vértices: "))

for i in range(qtd_vertices):
    vertice = input(f"Nome do vértice {i+1}: ")
    vertices.append(vertice)

qtd_arestas = int(input("Quantidade de arestas: "))
for i in range(qtd_arestas):
    origem = input("Origem: ")
    destino = input("Destino: ")
    peso = int(input("Peso da aresta: "))
    arestas.append((origem, destino, peso))

# ==========================
# EXECUÇÃO
# ==========================
origem = input("Vértice inicial: ")
resultado = bellman_ford(vertices, arestas, origem)

# ==========================
# SAÍDA
# ==========================
if resultado:

    print("\nMenores distâncias:")

    for vertice in resultado:

        print(f"{origem} -> {vertice} = {resultado[vertice]}")
