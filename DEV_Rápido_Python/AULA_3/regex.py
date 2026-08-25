import re

def verificar_regex(texto:str) -> None:
    padrao = r'\(\d{3}\) \d{3}-\d{4}'

    resultado = re.search(padrao, texto)
    if resultado:
        numero_telefone = resultado.group()
        print("Número de Telefone encontrado:", numero_telefone)
    else:
        print("Número de Telefone não encontrado.") 

if __name__=="__main__":
    verificar_regex("O número de telefone de Pedro é (123) 456-7890.")
