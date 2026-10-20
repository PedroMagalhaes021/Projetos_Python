import tkinter as tk

class GridApp:
    def __init__(self, raiz):
        for linha in range(3):
            for coluna in range(3):
                frame = tk.Frame(raiz, relief=tk.RAISED, bd=1)
                frame.grid(row=linha, column=coluna, padx=5, pady=5)
                texto = f"Linha {linha}\nColuna {coluna}"
                tk.Label(frame, text=texto).pack()


class GridResponsivoApp:
        def __init__(self, raiz):
            for posicao in range(3):
                raiz.columnconfigure(posicao, weight=1, minsize=75)
                raiz.rowconfigure(posicao, weight=1, minsize=50)
            for linha in range(3):
                for coluna in range(3):
                    texto = f"{linha}, {coluna}"
                    label = tk.Label(raiz, text=texto, relief=tk.RAISED)
                    label.grid(row=linha, column=coluna,
                                padx=5, pady=5, sticky="nsew")


class GradeApp:
    def __init__(self, raiz):
        raiz.title("Exemplo de sticky")
        raiz.columnconfigure(0,minsize=250)
        raiz.rowconfigure((0,1), minsize=100)
        a = tk.Label(raiz,text="A", bg="blue", fg="white")
        a.grid(row=0, column=0, sticky="ne")
        b = tk.Label(raiz, text="B", bg="blue", fg="white")
        b.grid(row=1,column=0, sticky="sw")


if __name__== "__main__":
    raiz = tk.Tk()
    GradeApp(raiz)
    raiz.mainloop()