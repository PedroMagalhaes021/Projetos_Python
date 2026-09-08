class Aluno:
    def __init__(self, nome: str, nota: list) -> None:
        self.nome = nome
        self.nota = nota
        
class ControleAlunos:
    def __init__(self):
        self.dicionario = {}
        
    def pedir_nota(self):
        contador = 0
        notas = []
        nome = input("Digite seu nome: ")
        while contador < 4:
            try:
                nota = float(input("Digite sua nota: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    contador += 1
                else:
                    print("Nota invalida! digite um valor entre 0 e 10")
            except ValueError:
                print("Erro ao colocar os valores")
            except Exception as e:
                print(f"Erro inesperado: {e}")
        
        aluno = Aluno(nome, notas)
        self.dicionario[nome] = aluno
        
    def criar_arquivo(self) -> None:
        try:
            with open("notas.txt", 'w', encoding="utf-8") as file:
                for nome, notaluno in self.dicionario.items():
                    file.write(f"Nome: {nome} | Notas: {notaluno.nota}\n")
            print("O arquivo 'notas.txt' foi criado com sucesso.")
        except PermissionError:
            print("Permissão negada para criar arquivo 'notas'.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado ao criar o arquivo 'notas': {e}")


if __name__ == "__main__":
    controle = ControleAlunos()
    controle.pedir_nota()
    controle.criar_arquivo() 
