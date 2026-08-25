import re

def pesquisar_email(texto:str,escondido:bool) -> None:
    padrao= r'\b[0-9._%+]+@[a-z]+\.[a-z]{3,}\b'

    if escondido:
        novo_texto = re.sub(padrao,"[email oculto]",texto)
        print("Resultado: ", novo_texto)
    else:
        emails_encontrados = re.findall(padrao,texto)
        if emails_encontrados:
            print("email encontrados:",",".join(emails_encontrados))
        else:
            print("Nenhum email encontrado.")

if __name__=="__main__":
    pesquisar_email("Meu email é exemplo@gmail.com, 22@66.88, 22@aa.bbb, entre em contato",True)
