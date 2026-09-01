from collections import defaultdict

def criar():
    notas=list(input("Digite a nota dos alunos:"))
    with open("notas.txt","w",encoding="utf-8")as arquivo:
        arquivo.write(notas)


    with open("notas.txt","r",encoding="utf-8")as arquivo:
        conteudo=arquivo.read()
        print("Conteudo do arquivo")
        print(conteudo)


teste=list(input("Digite a nota dos alunos:"))
print(teste)        
