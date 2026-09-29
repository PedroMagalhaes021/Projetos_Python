import dataset
import os

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
CAMINHO_BANCO = os.path.join(DIRETORIO_ATUAL, 'banco_dados.db')

db = dataset.connect(f'sqlite:///{CAMINHO_BANCO}')

def create(nome: str, telefone: int):
    table = db['CONTATOS']
    table.insert({"nome": nome, "telefone": telefone})
    print("dados criados com sucesso")

def procurar(nome_busca: str):
    table = db["CONTATOS"]
    procura = table.find_one(nome=nome_busca)
    return procura

def update(nome_busca, telefone_novo):
    table = db['CONTATOS']
    dados_atualizados = {"nome": nome_busca, "telefone": telefone_novo}
    table.update(dados_atualizados, ["nome"])
    print(f"Dados updated com sucesso:{nome_busca}")

def delete(nome_busca):
    table = db['CONTATOS']
    table.delete(nome=nome_busca)

if __name__ == "__main__":
    while True:
        opcao = input("""
            MENU CONTATOS
            1 - Procurar Contato
            2 - Adicionar Contato
            0 - Sair
            
            Digite uma opção: """)
        
       
        match opcao:
            case "1":
                nome = str(input("Digite o nome que deseja procurar no DB: "))
                dados = procurar(nome)
                if dados is not None:
                    print(dados)
                else:
                    print("Nome digitado Inexistente")
            case "2":
                nome=input("Digite o nome do contato que deseja Adicionar:")
                telefone=input("Digite o telefone do contato que deseja adicionar:")
                create(nome,telefone)
                    
            case "0":
                print("Saindo do programa...")
                break
                
            case _:
                print("Opção inválida! Tente novamente.")
