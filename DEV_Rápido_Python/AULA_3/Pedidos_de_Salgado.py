import time
from typing import Generator, Any


def get_coxinha(*pedidos) -> list:
    print("[Return] Preparando TODA a fornada de coxinhas de uma vez....")
    time.sleep(1)
    return[f'{pedido} coxinhas'for pedido in pedidos]

def get_joelho(*pedidos) -> Generator[Any,Any,Any]:
    for pedido in pedidos:
        print(f'---[Yield] Saindo um pedido de {pedido} joeho(s) agora!')
        time.sleep(1)
        yield f'{pedido} joelho(s)'

if __name__=="__main__":
    print("SOLICITANDO COXINHAS (Retun): ")
    salgados_return = get_coxinha(4,6,8)
    print("Recebi a lista Completa:", salgados_return)

    print("\n" + "="*30 + "\n")
    print("SOLICITANDO JOELHOS(Yield):")
    pedidos_joelho = get_joelho(4,6,8)
    for salgado in pedidos_joelho:
        print(f"Cliente Recebeu: {salgado}")
