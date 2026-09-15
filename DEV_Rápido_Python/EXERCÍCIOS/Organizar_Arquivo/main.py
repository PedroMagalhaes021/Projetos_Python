from pathlib import Path
from gerenciador_de_alunos import GerenciadorAlunos

def exibir_menu():
    print("\n--- Gerenciador de Alunos ---")
    print("1. Cadastrar Aluno")
    print("2. Listar Alunos")
    print("3. Buscar Aluno")
    print("4. Alterar Nota")
    print("5. Remover Aluno")
    print("0. Sair")
    return input("Escolha uma opção: ")

def main():
    base_dir = Path(__file__).parent
    gerenciador = GerenciadorAlunos(base_dir)

    while True:
        opcao = exibir_menu()

        match opcao:
            case "1":
                nome = input("Nome do aluno: ")
                try:
                    nota = float(input("Nota do aluno: "))
                    gerenciador.cadastrar(nome, nota)
                    print(f"Aluno {nome} cadastrado com sucesso!")
                except ValueError:
                    print("Erro: A nota deve ser um número.")

            case "2":
                print("\nLista de Alunos:")
                alunos = gerenciador.listar()
                if not alunos:
                    print("Nenhum aluno cadastrado.")
                else:
                    for aluno in alunos:
                        print(aluno)

            case "3":
                nome = input("Digite o nome para buscar: ")
                resultado = gerenciador.buscar(nome.strip().title())
                print(resultado)

            case "4":
                nome = input("Nome do aluno para alterar nota: ")
                try:
                    nova_nota = float(input("Digite a nova nota: "))
                    if gerenciador.alterar_nota(nome.strip().title(), nova_nota):
                        print("Nota atualizada!")
                    else:
                        print("Aluno não encontrado.")
                except ValueError:
                    print("Erro: A nota deve ser um número.")

            case "5":
                nome = input("Nome do aluno para remover: ")
                if gerenciador.remover(nome.strip().title()):
                    print(f"Aluno {nome} removido.")
                else:
                    print("Aluno não encontrado.")

            case "0":
                print("Saindo do sistema... Até logo!")
                break

            case _:
                print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
