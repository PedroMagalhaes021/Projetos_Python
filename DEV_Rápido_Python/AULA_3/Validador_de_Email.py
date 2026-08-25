import re

def validar_email():
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    email=input("Digite seu Email para confirmar Autenticidade:")
    resultado = re.match(padrao,email)
    if resultado is not None :
        print("email valido")
    else:
        print("email invalido")
    





if __name__ =="__main__":
    validar_email()
