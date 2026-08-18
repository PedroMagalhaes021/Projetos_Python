def escrita():

    with open('C:/Users/aluno/Desktop/Python/aula03/manipulando_arquivo/nomes.txt', 'w') as arquivo:
        arquivo.write("Ó o cara")
        arquivo.writelines(["\nÓ o cara 2 - O retorno","\nÓ o cara 3 - O inimigo agora é outro","\nÓ o cara 4 - Vida loka"])
    

    with open('C:/Users/aluno/Desktop/Python/aula03/manipulando_arquivo/nomes.txt') as arquivo:
        print(arquivo.readline())
    

def leitura():

    caminho_arquivo ='C:/Users/aluno/Desktop/Python/aula03/manipulando_arquivo/nomes.txt'

    with open (caminho_arquivo,'r') as arquivo:
        linhas=arquivo.readlines()
        for i, linha in enumerate(linhas, start=1):
            print(f'Linha{i}: {linha}')

if __name__ == "__main__":
    modo =['w','x','r','a']
    caminho = 'C:/Users/aluno/Desktop/Python/aula03/manipulando_arquivo/nomes.txt'
    escrita()
    leitura()
