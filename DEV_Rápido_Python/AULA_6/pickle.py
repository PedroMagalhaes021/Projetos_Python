import pickle

dados = {"nome": "Pedro","Idade" : "20","Profissão": "DEV"}

try: 
    with open("dados.bin","wb") as salva_binario:
        pickle.dump(dados, salva_binario)
    print("Dados salvos com sucesso")
except Exception as e:
    print(f"Ocorreu um erro ao salvar os dados: {e}")

try:
    with open("dados.bin","rb") as carrega_binario:
        dados_carregados = pickle.load(carrega_binario)
    print("Dados carregados com sucesso:",dados_carregados)
except Exception as e:
    print(f"Ocorreu um erro ao Carregar os dados: {e}")

if __name__ == "__main__":
    pass
