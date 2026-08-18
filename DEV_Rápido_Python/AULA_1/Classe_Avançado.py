from dataclasses import dataclass
@dataclass
class Aluno:
    nome:str
    idade:int
    notas:list
    def calcular(self):
        return sum(self.notas) / len(self.notas)
\

    if __name__ == "__main__":
        aluno1=Aluno("Kauã",20,[8,7,9,8])
        aluno2=Aluno("pedro",15,[6,7,3,8])
        lista_alunos=(aluno1,aluno2)
        for aluno in lista_alunos:
            print(f"Nome:{aluno.nome},média: {aluno.calcular_media():2.f}")
