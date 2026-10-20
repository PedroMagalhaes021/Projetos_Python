from dataclasses import dataclass
from datetime import date

@dataclass
class Pessoa:
    cpf:str
    nome:str
    nascimento:date
    oculos:bool
