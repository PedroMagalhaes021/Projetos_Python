from pathlib import Path
import json
from typing import List, Dict
from aluno import Aluno

class GerenciadorAlunos:    
    def __init__(self, base_dir: Path):
        self.csv_path = base_dir / "alunos.csv"
        self.json_path = base_dir / "alunos.json"
        self.txt_path = base_dir / "alunos.txt"
        self.alunos: Dict[str, float] = self._carregar()

    def _carregar(self) -> Dict[str, float]:
        if not self.csv_path.exists():
            return {}
        try:
            with open(self.csv_path, "r", encoding="utf-8") as f:
                dados = {}
                for linha in f:
                    if "," in linha:
                        nome, nota = linha.strip().split(",")
                        dados[nome] = float(nota)
                return dados
        except (ValueError, IndexError):
            print("Erro: Formato de dados inválido no CSV.")
        except IOError as e:
            print(f"Erro ao ler arquivo: {e}")
        return {}
    
    def salvar(self) -> None:
        try:
            lista_json = [{"nome": n, "nota": nt} for n, nt in self.alunos.items()]

            with open(self.csv_path, "w", encoding="utf-8") as f_csv, \
                 open(self.txt_path, "w", encoding="utf-8") as f_txt, \
                 open(self.json_path, "w", encoding="utf-8") as f_json:
                
                for nome, nota in self.alunos.items():
                    f_csv.write(f"{nome},{nota:.1f}\n")
                    f_txt.write(f"{nome} tem nota {nota:.1f}\n")
                
                json.dump(lista_json, f_json, indent=4, ensure_ascii=False)
        
        except PermissionError:
            print("Erro: Permissão negada ao salvar arquivos.")
        except OSError as e:
            print(f"Erro de sistema ao salvar: {e}")

    def cadastrar(self, nome: str, nota: float) -> bool:
        novo = Aluno(nome, nota)
        self.alunos[novo.nome] = novo.nota
        self.salvar()
        return True
    
    def remover(self, nome: str) -> bool:
        nome_formatado = nome.strip().title()
        if nome_formatado in self.alunos:
            del self.alunos[nome_formatado]
            self.salvar()
            return True
        return False
    
    def alterar_nota(self, nome: str, nova_nota: float) -> bool:
        nome_formatado = nome.strip().title()
        if nome_formatado in self.alunos:
            self.alunos[nome_formatado] = float(nova_nota)
            self.salvar()
            return True
        return False

    def listar(self) -> List[str]:
        return [f"{nome} - Nota: {nota:.1f}" for nome, nota in self.alunos.items()]

    def buscar(self, nome: str) -> str:
        nome_formatado = nome.strip().title()
        if nome_formatado in self.alunos:
            return f"Aluno: {nome_formatado}, Nota: {self.alunos[nome_formatado]:.1f}"
        return "Aluno não encontrado."
