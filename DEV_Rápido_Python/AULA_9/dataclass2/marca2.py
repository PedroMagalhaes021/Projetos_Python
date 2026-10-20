
from dataclasses import dataclass
from typing import ClassVar

@dataclass
class Marca:
    id:int
    nome:str
    sigla:str
    pais_origem:ClassVar[str]="Brasil"
