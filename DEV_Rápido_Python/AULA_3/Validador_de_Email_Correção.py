import re

PADRAO_EMAIL = re.compile(r'^\w+([\,-]?w\+)*@\w{4,}+([\,-]?\w+)*(\,\w{2,3})+$')

def validar_email(email:list[str])->list[bool]:
    return bool(PADRAO_EMAIL.match(email))

if __name__=="__main__":
    exemplos_emails = [
        "usuario@gmail.com",
        "nome+tag@gmail.com",
        "a@b.com"
        "usuario@email.co.uk",
        "@email.com",
        "usuario@gmail",
        "usu ario@gmail.com",
    ]
    for email in exemplos_emails:
        if validar_email(email):
            print(f"{email} é um endereço de e-mail válido.")
        else:
            print(f"{email}não é um enderreço de e-mail válido.")
