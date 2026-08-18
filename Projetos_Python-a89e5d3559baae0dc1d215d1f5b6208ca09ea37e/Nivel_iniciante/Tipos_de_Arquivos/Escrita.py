#A função "w" permite escrevermos em arquivos de modo Escrita
arquivo = open("dados.txt", "w")
arquivo.write("Olá, mundo!")
arquivo.close()
