import tkinter as tk
from tkinter import ttk

class AppMeses:
    def __init__(self,raiz):
        raiz.geometry("270x130")
        raiz.title("Exemplo Combobox")
        ttk.Label(raiz, text="Selecione um mês:").pack(pady=5)
        mese = ["janeiro","Fevereiro","Março","Abriu","Maio","Junho","julho","Agosto",
                "Setembro","outubro","Novembro","Dezembro"]
        self.combo = ttk.Combobox(raiz, values= mese,
                                  state="readonly")

        self.combo.pack(pady=5)
        self.combo.current(0)
        self.combo.bind("<<ComboboxSelected>>", self.selecionar)

    def selecionar(self,_):
        print(f"Mês escolhido: {self.combo.get()}")

if __name__ == "__main__":
    raiz = tk.Tk()
    AppMeses(raiz)
    raiz.mainloop()
