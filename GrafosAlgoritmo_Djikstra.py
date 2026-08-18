import heapq
#==================================
#FUNÇÃO DIJKSTRA
#===================================
def dijkstra(grafo,inicio):
    distancias={vertices:float('inf') for vertices in grafo}
    distancias[inicio]=0
    fila=[(0,inicio)]
    while fila:
        distancia_atual, vertice_atual, = heapq.heappop(fila)
        for vizinho, peso in grafo [vertice_atual]:
            nova_distancia = distancia_atual + peso
        if nova_distancia < distancias[vizinho]:
            distancias[vizinho] = nova_distancia
            heapq.heappush(fila, (nova_distancia,vizinho))
        return distancias
    
#====================================
#ENTRADA DE GRAFO
#====================================
grafo={}
qtd_vertices=int(input("Qunatidade de vértices: "))
 #Criando Vértices 
for i in range (qtd_vertices):
    vertice=input(f"Nome da vértice {i+1}: ")   
    grafo[vertice]=[]

qtd_arestas = int(input("Quantidade de Arestas: "))
#Inserindo Arestas
for i in range(qtd_arestas):
    origem=input("Origem: ")
    destino=input("Destino: ")
    peso=int(input("Peso da aresta: "))
    #Grafo Não Direcionado
    grafo[origem].append((destino,peso))
    grafo[destino].append((origem,peso))
#=======================================
#EXECUÇÃO
#======================================
inicio=input("Vértice inicial: ")
resultado=dijkstra(grafo,inicio)
print("\nMenores Distâncias: ")
for vertice, distancia in resultado.items():
    print(f"{inicio}->{vertice}={distancia}")
