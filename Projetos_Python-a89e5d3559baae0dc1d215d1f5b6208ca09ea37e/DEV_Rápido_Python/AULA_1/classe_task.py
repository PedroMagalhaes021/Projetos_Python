class task:
    def __init__(self, title, desc):
        self.title = title
        self.desc = desc
        self.conclu = False

    def marcar_conclu(self):
        self.conclu = True

    def __str__(self):
        status = "✔" if self.conclu else "✖"
        return f"[{status}] {self.desc}"

class taskmngr:
    def __init__(self):
        self.tarefas = []


    def add(self, title, desc):
        tarefa = task(title, desc)
        self.tarefas.append(tarefa)
        print(f"Tarefa '{desc}' adicionada.")


    def list(self):
        if not self.tarefas:
            print("Nenhuma tarefa a ser listada.")
            return
        print("Lista: ")
        for idx, tarefa in enumerate(self.tarefas, 1):
            print(f"{idx}. {tarefa}")

    def estado(self, indice):
        if 0 < indice <= len(self.tarefas):
            self.tarefas[indice - 1].marcar_conclu()
            print(f"Tarefa {indice} concluida.")
        else: 
            print("Indice inexistente...")


if __name__ == "__main__":
    gerenciador = taskmngr()

    gerenciador.add("Comprar leite", "Comprar leite na boca do k11")

    gerenciador.add("Estudar Python", "Estudar python para fazer sistema de venda de drogas para a boca do k11")

    gerenciador.list()

    gerenciador.estado(1)
    
    gerenciador.list()
