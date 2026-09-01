import time
import re 
from typing import Generator,Any



def verifica_regex(texto:str):
    padrao=r'\(\d{3}\) \d{3}-\d{4}'

    resultado=re.search(padrao,texto)


    if resultado:
        numero_telefone=resultado.group()
        print("Numero de telefone encontrado:",numero_telefone)
    else:
        print("Número de telefone nao encontrado")


def pesquisa_email(texto:str,escondido:bool):
    padrao=r'\b[0-9._%+-]+@[a-z]+\.[a-z]{3,}\b'


    if escondido:
        novo_texto=re.sub(padrao,"[email oculto]",texto)
        print("resultado :",novo_texto)
    else:
        emails_encontrados=re.findall(padrao,texto)
        if emails_encontrados:
            print("E-mails encontrados:",", ".join(emails_encontrados))
        else:
            print("Nenhum E-mail econtrado")

def get_coxinhas(*pedidos)->list:
    print("--- preparando fornada de coxinhas ")
    time.sleep(1)
    return[f'{pedido}coxinhas'for pedido in pedidos]


def get_joelhos(*pedidos)->Generator[Any,Any,Any]:
    for pedido in pedidos:
        print(f"----[yield] saindo um pedido de {pedido} joelhos agora")
        time.sleep(1)
        yield[f'{pedido} joelhos']


def string():
    texto="nossa"
    print(texto[2])

def manipulacao(recebido:str):
    print(recebido[0:20:2])

def mostrar_len(recebido:str):
    print(len(recebido))

def count(recbd:str):
    print(recbd.count("a"))

def count2(rec:str):
    print(rec.count("a",5,30))

def find(texto:str):
    print(texto.find("aula"))
    print(texto.find("Python"))


def usando_replace(rcbd):
    novo_txt=rcbd.replace("Manipulando","Trabalhando com")
    print(novo_txt)
    print(rcbd)


    print(rcbd.startswith("Nossa"))
    print(rcbd.startswith("aula"))
    print(rcbd.endswith("aula"))
    print(rcbd.endswith("."))


def metodos(recebido:str):
    print(recebido.lower())
    print(recebido.upper())
    print(recebido.capitalize())
    print(recebido.title())
    print(recebido.swapcase())

def remover_espacos_branco():
    nome=str(input("Digite seu nome:"))
    print(f"Ola {nome}!")
    print(f"ola, {nome.strip()}")
    print(nome.rstrip())
    print(nome.lstrip())
def usando_split(recebe:str):
    print(recebe.split())
def count_strip_split_join(recebe:str):
    print(' '.join(recebe))
    print(recebe.split())
    print(' '.join(recebe.split()))
if __name__ =="__main__":
    recebe1="Nossa aula Manipulando String"
    pesquisa_email("meu email é pintomole@gmail.com",True)
    verifica_regex("O numero de telefone de pintomole é (123) 456-7890.")
    print("Soliciando coxinhas (Return):")
    salgados_return=get_coxinhas(4,6,8)
    print("Recebi a lista completa :",salgados_return)

    print("\n"+"="*30+"\n")
    print("Solicitando Joelhos")
    pedidos_joelho=get_joelhos(4,6,8)
    for salgado in pedidos_joelho:
        print(f"Cliente recebeu:{salgado}")

    mostrar_len(recebe1)
    count(recebe1)
    count2(recebe1)
    find(recebe1)
    usando_replace(recebe1)
    manipulacao(recebe1)
    metodos(recebe1)
    string()
    usando_split(recebe1)
    count_strip_split_join(recebe1)
    remover_espacos_branco()
