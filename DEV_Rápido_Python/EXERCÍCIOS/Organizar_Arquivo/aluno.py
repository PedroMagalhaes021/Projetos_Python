from typing import Dict

class Aluno:
    def __init__(self, nome: str, nota: float):
        self.nome = nome.strip().title()
        self.nota = float(nota)
    
    def to_dict(self) -> Dict[str, float]:
        return {self.nome: self.nota}
 
    def __str__(self) -> str:
        return f"{self.nome},{self.nota:.1f}"
