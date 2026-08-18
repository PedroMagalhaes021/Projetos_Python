//
append(elemento): adiciona um elemento ao final da lista.
insert(indice, elemento): insere um elemento em uma posição específica da lista.
remove(elemento): remove a primeira ocorrência de um elemento na lista.
pop(indice): remove e retorna o elemento em uma posição específica da lista.
sort(): ordena os elementos da lista em ordem ascendente.
reverse(): inverte a ordem dos elementos na lista.
//
  
frutas = ["maçã", "banana", "laranja"]

frutas.append("pera")
print(frutas)  # Imprime ["maçã", "banana", "laranja", "pera"]

frutas.insert(1, "uva")
print(frutas)  # Imprime ["maçã", "uva", "banana", "laranja", "pera"]

frutas.remove("banana")
print(frutas)  # Imprime ["maçã", "uva", "laranja", "pera"]

fruta_removida = frutas.pop(2)
print(frutas)  # Imprime ["maçã", "uva", "pera"]
print(fruta_removida)  # Imprime "laranja"

frutas.sort()
print(frutas)  # Imprime ["maçã", "pera", "uva"]

frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "maçã"]
