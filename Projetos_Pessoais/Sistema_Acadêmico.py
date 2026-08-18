class Aluno:
    
    def __init__(self:object ,nome:str,idade:int,notas:float) -> None:
        self.nome = nome
        self.idade = idade
        self.notas = notas
        
    def calcular_media(self:object)->float:
        return sum(self.notas) / len(self.notas)
        
if __name__=="__main__":
    aluno1 = Aluno("Pedro", 20, [8.3, 7.5, 10])
    aluno2 = Aluno("Kaua", 18, [9.3, 9.5, 10])
    lista_alunos = [aluno1,aluno2]
    
    for aluno in lista_alunos:
        print(f"Nome:{aluno.nome}, Media:{aluno.calcular_media():.2f}")
