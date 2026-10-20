from datetime import date
from pessoa import Pessoa
from marca import Marca
from veiculo import Veiculo


pessoa1=Pessoa(cpf="12345678900",nome="kaua",nascimento=date(2006,7,20),oculos=True)

marca1=Marca(id=1,nome="Fiat",sigla="FIA")

veiculo1=Veiculo(placa="RMS2288",cor="Cinza",proprietario=pessoa1,marca=marca1)

print(pessoa1.nome)
