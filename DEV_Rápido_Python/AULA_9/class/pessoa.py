from datetime import date



class Pessoa:
    def __init__(self:object,cpf:str,nome:str,nascimento:date,oculos:bool)->None:
       self.cpf=cpf
       self.nome=nome
       self.nascimento=nascimento
       self.oculos=oculos
