import heapq

def prim(grafo, inicio):
    visitados =set()
    fila_prioridade = []
    visitados.add(inicio)

    for vizinho, peso in grafo [inicio]:
        heapq.heappush(fila_prioridade,(peso,inicio,vizinho))
    arvore_minima =[]
    custo_total = 0
    while fila_prioridade:
        peso,origem,destino = heapq.heappop(fila_prioridade)
        if destino not in visitados:
            visitados.add(destino)
            arvore_minima.append((origem,destino,peso))
            custo_total += peso 
            for vizinho, peso_aresta in grafo [destino]:
                if vizinho not in visitados:
                    heapq.heappush(
                        fila_prioridade,
                        (peso_aresta,destino,vizinho)
                    )
    return arvore_minima, custo_total

#Programa Prinicpal

print("="*60)
print("Algoritmo de Prim - Grafo não direcionado")
print("="*60)

while True:
    try:
        num_vertices = int(input("Digite o número de Vértices: "))
        if num_vertices <= 0:
            print("ERRO: O npumero de vértices deve seer maior que zero.\n")
        else:
            break
    except ValueError:
        print("ERRO: Digite apenas números Inteiros.\n")

while True:
    try:
        num_arestas = int(input("Digite o número de Arestas: "))
        if num_arestas <= 0:
            print("ERRO: O número de arestas deve ser maior que zero.\n")
        else: 
            break
    except ValueError: 
        print("ERRO: Digite apenas Números inteiros.\n")

grafo = {}

for i in range (1,num_vertices+1):
    grafo[i]=[]
    print("\nDigite as arestas no formato: ")
    print("origem destino peso")
    print("Exemplo: 1 2 10 \n")

for i in range (num_arestas):
    print(f"\narestas{i+1}")
    while True:
        try:
            origem =int(input("Origem: "))
            destino =int(input("Destino: "))
            if origem not in grafo:
                print(f"ERRO: O vértice {origem} não existe.")
                print(f"Os vértices válidos vão de 1 até {num_vertices}.\n")
                continue
            if destino not in grafo:
                print(f"O vértice {destino} não existe.")
                print(f"os vértices vão de 1 até {num_vertices}.\n")
                continue    
            peso = float(input("Peso: "))
            #adicionar aresta no grafo
            grafo[origem].append((origem, peso))
            grafo[destino].append((destino, peso))
            break
        except ValueError:
            print("ERRO: Entrada Inválida. Digite números corretamente.\n")

vertice_inicial = 1

agm,custo_total = prim(grafo,vertice_inicial)

print("\n" + "="*60)
print("ÁRVORE GERADORA MÍNIMA(PRIM)")
print("="*60)
for origem,destino,peso in agm:
    print(f"{origem}---{destino} | Peso = {peso}")
print ("-" *60)
print(f"custo total da AGM: {custo_total}")
