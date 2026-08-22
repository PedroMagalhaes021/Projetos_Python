def sinonimos (dicionario):
    for i in dicionario:
        print(f"sinonimo {i}: {dicionario[i]}")

def ad_palavra (result):

    palavra = input ("Digite uma Palavra: \n").strip().lower()
    sinonimo_palavra = input ("Digite um Sinônimo: \n").strip().lower()

    if palavra in result:
        print ("Palavra já existe no dicionário")
    else:
        for i in result:
            existe = result[i]

            if sinonimo_palavra in existe:
                print ("Palavra já existe no dicionário")
                return
        result[palavra] = [sinonimo_palavra]

        print(f"{palavra} adicionada com sucesso!")

def buscar_sinonimo (dict):
    print("Digite a palavra que deseja buscar o sinônimo: ")
    for i in dict:
        print(i)
        escolha = input ("Digite a palavra: \n").strip().lower()
        if dict.get(escolha):
            print(f"Sinônimo de {escolha}: {dict[escolha]}")
        else:
            print(f"Não Encontramos o sinônimo de {escolha} no dicionário")

def deletar (dicionario2):
    print("Digite a palavra que deseja deletar: ")
    for i in dicionario2:
        print(i)
    deletar = input ("Digite a palavra: \n").strip().lower()
    if dicionario2.get(deletar):
        del dicionario2[deletar]
        print(f"{deletar} deletada com sucesso!")
    else:
        print(f"Não Encontramos a palavra {deletar} no dicionário")

if __name__ == "__main__":
    dicionario = {}
    while True:
        print("Escolha uma opção: ")
        print("1 - Adicionar palavra")
        print("2 - Buscar sinônimo")
        print("3 - Deletar palavra")
        print("4 - Listar palavras e sinônimos")
        print("5 - Sair")

        escolha = input("Digite a opção desejada: \n").strip()

        if escolha == "1":
            ad_palavra(dicionario)
        elif escolha == "2":
            buscar_sinonimo(dicionario)
        elif escolha == "3":
            deletar(dicionario)
        elif escolha == "4":
            sinonimos(dicionario)
        elif escolha == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
