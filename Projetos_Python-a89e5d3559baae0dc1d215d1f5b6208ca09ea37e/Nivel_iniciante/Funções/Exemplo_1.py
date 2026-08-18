# função para calcular a média de vários números
def calcular_media(*numeros):
    soma = sum(numeros)
    quantidade = len(numeros)
    media = soma / quantidade
    return media
#saída de Resultado da média com os 4 número passados como argumento
print("Media: ", calcular_media(10,20,30,40))
#Função de soma de 3 usando lambda
def soma_3(x):
    return x + 3
#criando a Lambda para somar 3
soma = lambda x: x + 3
#Executando a função soma para o número 5
print("Somando 3: ", soma(5))
