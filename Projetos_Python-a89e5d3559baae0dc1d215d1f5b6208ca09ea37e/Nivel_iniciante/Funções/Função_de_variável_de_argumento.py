#função de variavel de argumento
def soma_variavel(*numeros):
    total = 0 
    for numero in numeros:
        total += numero
    return total

print(soma_variavel(1, 2, 3, 4, 5)) # Saída: 15 
print(soma_variavel(10, 20)) # Saída: 30  
