from dataclasses import dataclass


@dataclass(slots=True,frozen=True)
class Marca:
    id:int
    nome:str
    sigla:str
