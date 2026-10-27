import tkinter as tk
from tkinter import ttk

class AbasApp:

    def __init__(self,raiz):
        raiz.title("Dashboard com abas")
        abas = ttk.Notebook(raiz)
        principal = ttk.Frame(abas)
        sobre = ttk.Frame(abas)
        abas.add(principal, text="Principal")
        abas.pack(expand=True, fill="both")
        ttk.Label(principal, text="Conteudo principal").pack(padx=20,pady=20)
        ttk.Label(sobre, text="Sobre o sistema").pack(padx=20,pady=20)

if __name__ == "__main__":
    raiz = tk.Tk()
    AbasApp(raiz)
    raiz.mainloop()
