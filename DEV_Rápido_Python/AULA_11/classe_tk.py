import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self, raiz):
        self.label = ttk.Label(raiz, text="Pronto!")
        self.label.pack(pady=12)
        ttk.Button(raiz, text="Clique",
                   command=self.clicar).pack()

    def clicar(self):
        self.label.config(text="Você Clicou!")

if __name__== "__main__":
    raiz = tk.Tk()
    App(raiz)
    raiz.mainloop()
