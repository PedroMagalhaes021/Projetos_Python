#Jogo da Forca

#Lógicas
#Palavaras Secretas
#Tentativas Limitadas 
#Mostrar Progresso 

import random

temas = {
    "1": {"nome": "frutas", "palavras": ["abacate","abacaxi","maçã","laranja","mamão","morango"]},
    "2": {"nome": "filmes", "palavras": ["homem-aranha","homem de ferro","harry potter","interestelar","percy jackson","ratatouile"]},
    "3": {"nome": "animais", "palavras": ["aranha","elefante","papagaio","rena","jacaré","leão"]},
    "4": {"nome": "países", "palavras": ["itália","frança","japão","brasil","méxico","inglaterra"]},
    "5": {"nome": "famosos", "palavras": ["tom holland","andrew garfield","sabrina carpenter","madonna","michael jackson","neymar"]}
}

def jogar():
    # Sorteio
    tema_escolhido = random.choice(list(temas.keys()))
    palavra_secreta = random.choice(temas[tema_escolhido]["palavras"])

    print(f"\nTema sorteado: {temas[tema_escolhido]['nome']}")

    # Variáveis
    letras_acertadas = []
    letras_erradas = []
    tentativa = 15

    # Função interna
    def mostrar_palavra():
        palavra_formada = ""
        for letra in palavra_secreta:
            if letra == " " or letra == "-":
                palavra_formada += letra + " "
            elif letra in letras_acertadas:
                palavra_formada += letra + " "
            else:
                palavra_formada += "_ "
        return palavra_formada

    # Loop do jogo
    while tentativa > 0:
        print("\nPalavra:", mostrar_palavra())
        print("Letras erradas:", letras_erradas)

        letra = input("Digite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Digite apenas UMA letra válida!")
            continue 

        if letra in letras_acertadas or letra in letras_erradas:
            print("Você já utilizou esta letra!")
            continue

        if letra in palavra_secreta:
            letras_acertadas.append(letra)
            print("A letra está correta!")
        else:
            letras_erradas.append(letra)
            tentativa -= 1
            print(f"Você errou! Tentativas restantes: {tentativa}")

        if "_" not in mostrar_palavra():
            print("\nParabéns, você venceu!")
            print("A palavra era:", palavra_secreta)
            return

    print("\nVocê perdeu!")
    print("A palavra era:", palavra_secreta)


# Jogar novamente
while True:
    jogar()

    resposta = input("\nQuer jogar novamente? (s/n): ").lower()

    if resposta != "s":
        print("Obrigado por jogar!")
        break
