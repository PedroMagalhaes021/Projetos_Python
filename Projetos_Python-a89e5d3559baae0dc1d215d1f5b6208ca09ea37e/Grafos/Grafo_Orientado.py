#include <stdio.h>
#include <stdlib.h>

#define MAX 100

// Nó da lista adjacência
typedef struct No {
    int vertice;
    struct No* prox;
} No;

// Estrutura do grafo
typedef struct {
    int numVertices;
    No* listaAdj[MAX];
} Grafo;

// Criar Grafo
Grafo* criarGrafo(int vertices) {
    Grafo* g = (Grafo*)malloc(sizeof(Grafo));
    if (g == NULL) {
        printf("Erro de memoria\n");
        exit(1);
    }
    g->numVertices = vertices;
    // Correção: i < vertices, inicializando listas
    for (int i = 0; i < vertices; i++) {
        g->listaAdj[i] = NULL;
    }
    return g;
}

// Criar Novo Nó
No* criarNo(int v) {
    No* novo = (No*)malloc(sizeof(No));
    novo->vertice = v;
    novo->prox = NULL;
    return novo;
}

// adicionar aresta(orientado: só um sentido)
void adicionarAresta(Grafo* g, int v1, int v2) {
    if (v1 >= g->numVertices || v2 >= g->numVertices || v1 < 0 || v2 < 0) {
        printf("Vertice invalido!\n");
        return;
    }
    // Correção: passa v2 (destino) para o novo nó
    No* novo = criarNo(v2);
    novo->prox = g->listaAdj[v1];
    g->listaAdj[v1] = novo;
}

// imprimir grafo
void imprimirGrafo(Grafo* g) {
    printf("\nLista de adjacencia:\n");
    for (int i = 0; i < g->numVertices; i++) {
        printf("%d", i);
        No* temp = g->listaAdj[i];
        while (temp != NULL) {
            printf(" -> %d", temp->vertice);
            temp = temp->prox;
        }
        printf(" -> NULL\n");
    }
}

// liberar a memoria
void liberarGrafo(Grafo* g) {
    for (int i = 0; i < g->numVertices; i++) {
        No* temp = g->listaAdj[i];
        while (temp != NULL) {
            No* aux = temp;
            temp = temp->prox;
            free(aux);
        }
    }
    free(g);
}

int main() {
    int vertices, arestas;
    int v1, v2;

    printf("Numero de vertices: ");
    if (scanf("%d", &vertices) != 1) return 1;

    Grafo* g = criarGrafo(vertices);

    printf("Numero de Arestas: ");
    if (scanf("%d", &arestas) != 1) return 1;

    for (int i = 0; i < arestas; i++) {
        printf("Aresta %d (origem destino): ", i + 1);
        scanf("%d %d", &v1, &v2);
        adicionarAresta(g, v1, v2);
    }

    imprimirGrafo(g);
    liberarGrafo(g);

    return 0;
}
