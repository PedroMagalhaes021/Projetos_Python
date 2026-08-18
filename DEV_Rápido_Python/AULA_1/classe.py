class aluno:
    def __init__(self, nome, n1, n2, n3, n4):
        self.nota1 = n1
        self.nota2 = n2
        self.nota3 = n3
        self.nota4 = n4
        self.nome = nome

    def media(self): return (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4

    def resultado(self):
        if self.media < 7:
            print("Não aprovado, dá pra ser vapor na favela.")

        else:
            print("Aprovado, vai vira gerente da boca.")

    def __str__(self):
         return f"Aluno: {self.nome}\nMédia: {self.media():.2f}\n Resultado: {self.resultado()}"        

if __name__ == "__main__": 
    nome = input("Nome do aluno: ") 
    
    nota1 = float(input("Digite a primeira nota: ")) 
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: ")) 
    nota4 = float(input("Digite a quarta nota: ")) 
    aluno = aluno(nome, nota1, nota2, nota3, nota4) 
    print("\n--- Resultado ---") 
    print(aluno)
