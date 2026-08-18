frutas = {"maçã", "banana", "laranja"}
numeros = set([1, 2, 3, 4, 5])

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

uniao = conjunto1 | conjunto2
print(uniao)  # Imprime {1, 2, 3, 4, 5}

intersecao = conjunto1 & conjunto2
print(intersecao)  # Imprime {3}

diferenca = conjunto1 - conjunto2
print(diferenca)  # Imprime {1, 2}

diferenca_simetrica = conjunto1 ^ conjunto2
print(diferenca_simetrica)  # Imprime {1, 2, 4, 5}
