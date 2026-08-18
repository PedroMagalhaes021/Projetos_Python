#include <stdio.h>
#include <stdlib.h>
#define MAX 100

typedef struct{
    int numVertices;
    int matrizAdj[MAX][MAX];
}Grafo;

//função para criar Grafo

Grafo* criarGrafo(int vertices){
    Grafo*g=(Grafo*)malloc(sizeof(Grafo));
    if(g==NULL){
        printf("Erro de Memoria\n");
        exit(1);
}
 g->numVertices=vertices;
 //inicializa com 100
 for(int i=0; i<vertices;i++){
 for(int j=0; j<vertices;j++ ){
 g->matrizAdj[i][j]=0;
}
}
return g;
}
void adicionarAresta(Grafo* g,int v1,int v2){
    if(v1>=g->numVertices|| v2>=g->numVertices){
        printf("Vertice Invalido\n");
        return;
    }
    g->matrizAdj[v1][v2]=1;
    g->matrizAdj[v2][v1]=1;
}
void imprimirGrafo(Grafo*g){
    printf("\nMatriz De Adjacencia:\n");
    for(int i=0;i<g->numVertices;i++){
    for(int j=0; j<g->numVertices;j++){
        printf("%d",g->matrizAdj[i][j]);
    }
    printf("\n");
    }
}


int main(){
    int vertices,arestas;
    int v1,v2;
    printf("Numero de vertices: ");
    scanf("%d",&vertices);
    Grafo*g=criarGrafo(vertices);
    printf("Numeros De Arestas: ");
    scanf("%d",&arestas);
    for(int i=0;i<arestas;i++){
        printf("Aresta %d(v1 v2):",i+1);
        scanf("%d%d",&v1,&v2);
        
        adicionarAresta(g,v1,v2);
        }
        imprimirGrafo(g);
        free(g);
        return 0;
    return 0;
}
