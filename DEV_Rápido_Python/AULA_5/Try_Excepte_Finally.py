def divide(x,y):
    try:
        resultado=x/y
    except ZeroDivisionError:
        print("Opa,para aí,Voce esta tentando dividir por zero")
    else:
        print("Certa a sua resposta:",resultado)
    finally:
        print("isso sempre acontecera")


def abrir():
    try:
        f= open('nomes.txt')
        s=f.readline()
        i=int(s.strip())
    except FileExistsError:
        print("Arquivo 'nomes.txt' ja existe")
    except IOError:
        print("Erro abertura do arquivo")
    except ValueError:
        print("Formato invalido encontado no arquivo")
    except  Exception as e:
        print(F"Erro inesperado{e}")
        raise



abrir()
