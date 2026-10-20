from dataclasses import dataclass
from pessoa import Pessoa
from marca import Marca


@dataclass
class Veiculo:
    placa:str
    cor:str
    proprietario:Pessoa
    marca:Marca
    
