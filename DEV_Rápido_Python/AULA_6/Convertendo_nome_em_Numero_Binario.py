import os 
def dados():
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    dados_binario_nome = os.path.join(diretorio_atual, "dados_puros.bin")

    frase = "Pedro Cordeiro de Jesus Veras Magalhães"
    dados_binarios = frase.encode('utf-8')

    try:
        with open (dados_binario_nome,'wb') as salva_binario:
            salva_binario.write(dados_binarios)
        print("Dados binarios salvos com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar os dados binários: {e}")
    if os.path.exists(dados_binario_nome):
        try:
            with open(dados_binario_nome, "rb") as carrega_binario:
                dados_carregados_bytes = carrega_binario.read()

                #1 Decodfica
                dados_carregados_texto = dados=dados_carregados_bytes.decode('utf-8')

                #2 Converte os bytes 
                binario_real = " ".join(f"{byte:08b}" for byte in dados_carregados_bytes)

            print("Dados carregados com sucesso:")
            print(f"{binario_real} -> {dados_carregados_texto}")
        except Exception as e:
            print(f"Ocorreu um erro ao carregar os dados binários: {e}")

if __name__ =="__main__":
    dados()
