from json import JSONDecodeError

from contato import Contato
from controle_contatos import ControleContatos


ARQUIVO_JSON = "contatos.json"
ARQUIVO_TXT = "contatos.txt"


def salvar_dados(controle: ControleContatos) -> None:
    controle.salvar_json(ARQUIVO_JSON)
    controle.salvar_txt(ARQUIVO_TXT)


def cadastrar(controle: ControleContatos) -> None:
    print("\n--- NOVO CONTATO ---")

    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    email = input("E-mail: ")
    telefone = input("Telefone: ")

    contato = Contato(
        nome,
        sobrenome,
        email,
        telefone
    )

    controle.adicionar(contato)

    salvar_dados(controle)

    print("\nContato cadastrado com sucesso.")


def buscar(controle: ControleContatos) -> None:
    termo = input(
        "\nDigite nome, e-mail ou telefone: "
    )

    contatos = controle.buscar(termo)

    if not contatos:
        print("Nenhum contato encontrado.")
        return

    print("\n--- RESULTADO ---")

    for contato in contatos:
        print(contato)


def listar(controle: ControleContatos) -> None:
    contatos = controle.listar()

    if not contatos:
        print("\nAgenda vazia.")
        return

    print("\n--- CONTATOS ---")

    for numero, contato in enumerate(
        contatos,
        start=1
    ):
        print(f"{numero}. {contato}")


def remover(controle: ControleContatos) -> None:
    email = input(
        "\nInforme o e-mail do contato: "
    )

    contato = controle.remover(email)

    salvar_dados(controle)

    print(
        f"\n{contato.nome_completo} removido com sucesso."
    )


def mostrar_menu() -> None:
    print(
        """
==============================
       AGENDA DE CONTATOS
==============================

1 - Adicionar contato
2 - Buscar contato
3 - Listar contatos
4 - Remover contato
5 - Carregar dados do TXT
0 - Sair
"""
    )


def carregar_dados(
    controle: ControleContatos
) -> None:

    try:
        erros = controle.carregar_json(
            ARQUIVO_JSON
        )

        print(
            f"{len(controle.contatos)} "
            "contato(s) carregado(s)."
        )

        if erros:
            print("\nAlguns registros foram ignorados:")

            for erro in erros:
                print(f"- {erro}")

    except FileNotFoundError:
        print(
            "Arquivo JSON ainda não existe. "
            "Uma nova agenda será criada."
        )

    except JSONDecodeError:
        print(
            "O arquivo contatos.json está "
            "corrompido ou possui JSON inválido."
        )

    except PermissionError:
        print(
            "Sem permissão para acessar "
            "contatos.json."
        )

    except ValueError as erro:
        print(f"Erro no arquivo: {erro}")


def main() -> None:
    controle = ControleContatos()

    carregar_dados(controle)

    while True:

        mostrar_menu()

        opcao = input("Escolha uma opção: ").strip()

        try:

            match opcao:

                case "1":
                    cadastrar(controle)

                case "2":
                    buscar(controle)

                case "3":
                    listar(controle)

                case "4":
                    remover(controle)

                case "5":
                    erros = controle.carregar_txt(
                        ARQUIVO_TXT
                    )

                    print(
                        f"\n{len(controle.contatos)} "
                        "contato(s) carregado(s) do TXT."
                    )

                    if erros:
                        print(
                            "\nRegistros ignorados:"
                        )

                        for erro in erros:
                            print(f"- {erro}")

                    salvar_dados(controle)

                case "0":
                    salvar_dados(controle)

                    print(
                        "\nDados salvos. "
                        "Programa encerrado."
                    )

                    break

                case _:
                    print(
                        "\nOpção inválida."
                    )

        except ValueError as erro:
            print(
                f"\nDados inválidos: {erro}"
            )

        except TypeError as erro:
            print(
                f"\nErro de tipo: {erro}"
            )

        except LookupError as erro:
            print(
                f"\n{erro}"
            )

        except FileNotFoundError:
            print(
                "\nArquivo não encontrado."
            )

        except PermissionError:
            print(
                "\nO programa não possui permissão "
                "para acessar o arquivo."
            )

        except OSError as erro:
            print(
                f"\nErro de acesso ao arquivo: {erro}"
            )


if __name__ == "__main__":
    main()
