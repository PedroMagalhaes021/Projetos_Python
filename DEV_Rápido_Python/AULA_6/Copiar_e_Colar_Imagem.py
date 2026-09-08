import os 
def copia():
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))

    imagem_entrada_nome = os.path.join(diretorio_atual, "images.jpg")
    imagem_saida_nome = os.path.join(diretorio_atual, "imagem_copia.jpg")

    if os.path.exists(imagem_entrada_nome):
        try:
            with open(imagem_entrada_nome, "rb") as imagem_entrada:
                with open(imagem_saida_nome, "wb") as imagem_saida:
                    imagem_saida.write(imagem_entrada.read())
            print("Imagem copiada com sucesso!")
        except Exception as e:
            print(f"Ocorreu um erro ao copiar uma imagem: {e}")
    else:
        print(f"A imagem '{imagem_entrada_nome}' não foi encontrada na pasta. ")

if __name__ =="__main__":
    copia()
