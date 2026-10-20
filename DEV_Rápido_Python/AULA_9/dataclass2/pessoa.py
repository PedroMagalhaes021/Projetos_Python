from dataclasses import dataclass,field
from datetime import date
from typing import List,Optional

@dataclass
class Pessoa:
    cpf:str
    nome:str
    nascimento:date
    oculos:bool
    cidade:Optional[str]=None

    _multas:List[str]=field(default_factory=list)
