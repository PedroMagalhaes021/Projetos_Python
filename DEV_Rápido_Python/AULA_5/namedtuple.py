from collections import namedtuple


Ponto=namedtuple('Ponto',['x','y'])


def coordenadas_local(x:float,y:float):
    meu_ponto=Ponto(x,y)
    return meu_ponto




if __name__ == "__main__":
    resultado=coordenadas_local(10.5,20.8)


    print(f"Acessando por nome(.x): {resultado.x}")

    print(f"Acessando por índice([1]):{resultado[1]}")

    print(f"Objeto completo:{resultado}")
