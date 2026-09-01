from collections import deque
def gerenciar_historico(paginas:list,nova_pagina:str) ->deque:
    historico=deque(paginas,maxlen=3)
    print(f"Historico inicial: {list(historico)}")
    historico.append(nova_pagina)
    print(f"Adicionadando '{nova_pagina}'\n\n....\n Historico agora :{list(historico)}")



def gerenciar_fila_atendimento(nomes:list,prioritario:str)->tuple:
    fila=deque(nomes)

    fila.appendleft(prioritario)


    quem_saiu=fila.pop()
    return fila,quem_saiu



if __name__ == "__main__":
    paginas_visitadas=["página 1","página 2","página 3"]
    meu_historico=gerenciar_historico(paginas_visitadas,"página 4")
    print("-"*30)
    clientes=["Samira","Juliana","Caroline"]
    fila_final,atendido=gerenciar_fila_atendimento(clientes,"Mayara")
    print(f"Fila de espera : {list(fila_final)}")
    print(f"Usuário Removido da ponta: {atendido}")
