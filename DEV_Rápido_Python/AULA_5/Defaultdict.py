from collections import defaultdict



def salas_de_aula(estudantes:list,salas:list)->dict:
    estudantes_por_sala=defaultdict(list)
    num_salas=len(salas)


    for i,estudante in enumerate(estudantes):

        sala_destino=salas[i % num_salas]
        estudantes_por_sala[sala_destino].append(estudante)
    return dict(estudantes_por_sala)


if __name__ == "__main__":
    alunos=["Kaua","Raphael","Sara","Cleber","Joao"]
    salas=["307A","308A"]
    print(salas_de_aula(alunos,salas))
