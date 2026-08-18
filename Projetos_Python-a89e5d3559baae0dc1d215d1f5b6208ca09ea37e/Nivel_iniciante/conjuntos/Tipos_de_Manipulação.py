//
add(elemento): adiciona um elemento ao conjunto.
remove(elemento): remove um elemento do conjunto. Se o elemento não existir, gera um erro.
discard(elemento): remove um elemento do conjunto se estiver presente. Se o elemento não existir, não faz nada.
clear(): remove todos os elementos do conjunto.
//
  frutas = {"maçã", "banana", "laranja"}


frutas.add("pera")
print(frutas)  # Imprime {"maçã", "banana", "laranja", "pera"}


frutas.remove("banana")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}


frutas.discard("uva")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}


frutas.clear()
print(frutas)  # Imprime set()
