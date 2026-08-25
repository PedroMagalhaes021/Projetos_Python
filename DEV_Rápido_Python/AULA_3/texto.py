def usando_len(lenzinho:str):
    print(len(lenzinho))
    
def usando_count(plr:str):
    print(plr.count("a"))
    print(plr.count("a",5,30))
    
def usando_find(passando_find:str):

    print(passando_find.find("Aula"))
    print(passando_find.find("Python"))
    print('String' in passando_find )
    print("Pedro" in passando_find)
    
def usando_replace(rcbd:str):
    novo_txt = rcbd.replace("Manipulando","Trabalhando com")
    print(novo_txt)
    print(rcbd)
    
    print(rcbd.startswith("Nossa"))
    print(rcbd.startswith("Aula"))
    print(rcbd.endswith("Aula"))
    print(rcbd.endswith("."))
    
def manipulando_texto(txt):

    print(txt.lower())
    print(txt.upper())
    print(txt.capitalize())
    print(txt.title())
    print(txt.swapcase())
    
def retirada():
    nome=str(input('DIGITE SEU NOME: '))
    print(f"olá, {nome}!")
    print(f'olá, {nome.strip()}!')  

    print(nome.strip())
    print(nome.lstrip())    
    
def utilizando_lista(rcb_lista):
    print(rcb_lista.split())

def utilizando_join(rcb_entrada):
    print(''.join(rcb_entrada))
    print(rcb_entrada.split())
    print(''.join(rcb_entrada.split()))
    
if __name__ =="__main__":

    recebe1 = "Nossa Aula Manipulando String."

    usando_replace(recebe1)
    usando_count(recebe1)
    usando_find(recebe1)
    usando_len(recebe1)
    manipulando_texto(recebe1)
    utilizando_lista(recebe1)
    utilizando_join(recebe1)
    retirada()
