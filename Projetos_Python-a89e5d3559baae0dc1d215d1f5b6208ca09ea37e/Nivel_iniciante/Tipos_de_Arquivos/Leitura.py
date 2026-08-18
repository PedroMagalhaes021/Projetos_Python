#O "r" é a função de leitura de arquivos txt.
arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
print(conteudo)
#A função clove serve para travar o arquivo e NÃO permitir que o usuário modifique o texto dentro do arquivo
arquivo.close()
