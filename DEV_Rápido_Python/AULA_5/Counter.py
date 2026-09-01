from collections import Counter



def funcao_corta_palavras(texto:str)->int:
    palavras=texto.lower().split()
    contagem=Counter(palavras)
    return contagem



if __name__ =="__main__":
    texto="Maçã banana maçã laranja banana maçã"
    print(funcao_corta_palavras(texto))
    print(funcao_corta_palavras(texto).most_common(2))
