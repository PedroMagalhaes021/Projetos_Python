def exemplo(nome,tipo):

    arquivo = open(nome,tipo)

    print('Nome do arquivo: ', arquivo.name)
    print('Tamanho do Arquivo: ', arquivo.tell())
    print('Modo do Arquivo: ', arquivo.mode)
    print('Arquivo está fechado? ', arquivo.closed)

    arquivo.close()

    print('Arquivo está fechado?', arquivo.closed)

if __name__ == "__main__":
    modo = ['w','r','x','a']
    caminho ='C:/Users/aluno/Desktop/Python/aula03/manipulando_arquivo/dados.txt'
    exemplo(caminho,modo[1])
